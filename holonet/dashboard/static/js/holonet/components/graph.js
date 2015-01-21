/** @jsx React.DOM */

var React = require('react');
var ReactBootstrap = require('react-bootstrap');
var request = require('superagent');
var cookie = require('cookie');

var Grid = ReactBootstrap.Grid;
var Row = ReactBootstrap.Row;
var Col = ReactBootstrap.Col;
var Modal = ReactBootstrap.Modal;
var ModalTrigger = ReactBootstrap.ModalTrigger;
var Button = ReactBootstrap.Button;
var Input = ReactBootstrap.Input;


var emailSeriesSpam = [];
var emailSeriesBlacklisted = [];
var emailSeriesBounce = [];

var Graph = React.createClass({

    getPayload: function() {
        return {
            "query": this.state.searchValue,
            "time_from": new Date().getTime()-this.state.timePicker,
            "time_to": new Date().getTime(),
            "spam": this.state.spam,
            "blacklisted": this.state.blacklisted,
            "bounce": this.state.bounce
        }
    },

    query: function() {
        var self = this;
        var cookies = cookie.parse(document.cookie);
        request
            .post('/api/graph/load/')
            .set('Accept', 'application/json')
            .set('X-CSRFToken', cookies['csrftoken'])
            .send(self.getPayload())
            .end(function(error, res){
                var response = res.body;

                var emails = response.hits.hits;
                var sources = emails.map(function(obj) {
                    return obj['_source'];
                });

                self.setState({
                    payload: response,
                    emails: sources
                });

                self.mapEmailSeries(response.aggregations);

            });
    },

    reloadData: function () {
        if (this.state.autorefresh) {
            this.query();
        }
    },

    getDefaultProps: function() {
        return {
            types: ['Spam', 'Bounce', 'Blacklisted'],
            timespans: [
                ['Last 6 hours', 21600000],
                ['Last day', 86400000],
                ['Last week', 604800000],
                ['Last month', 2419200000],
                ['Last year', 29030400000]
            ]
        }
    },

    changeTimespan: function(interval) {
        this.setState({
            timePicker: interval
        });
    },

    changeType: function(item) {
        if (item == 'Spam') {
            this.setState({spam: !this.state.spam})
        }
        else if (item == 'Bounce') {
            this.setState({bounce: !this.state.bounce})
        }
        else if (item == 'Blacklisted') {
            this.setState({blacklisted: !this.state.blacklisted})
        }
    },

    getInitialState: function() {

        return {
            spam: true,
            bounce: true,
            blacklisted: true,
            timePicker: 21600000,
            emails: [],
            searchValue: '',
            autorefresh: false

        };
    },

    componentDidMount: function () {

        this.interval = setInterval(this.reloadData, 10000);

        this.palette = new Rickshaw.Color.Palette( { scheme: 'spectrum2000' } );

        this.graph = new Rickshaw.Graph( {
            element: document.querySelector("#emailgraph"),
            renderer: 'bar',
            stack: true,
            height: '400',
            series: [{
                        data: emailSeriesSpam,
                        color: this.palette.color(),
                        name: 'Spam'
                    }, {
                        data: emailSeriesBounce,
                        color: this.palette.color(),
                        name: 'Bounce'
                    }, {
                        data: emailSeriesBlacklisted,
                        color: this.palette.color(),
                        name: 'Blacklisted'
                    }]
        });
        this.graph.render();

        this.xAxis = new Rickshaw.Graph.Axis.Time({
            graph: this.graph
        });
        this.xAxis.render();

        this.yAxis = new Rickshaw.Graph.Axis.Y({
            graph: this.graph
        });
        this.yAxis.render();

        this.hoverDetail = new Rickshaw.Graph.HoverDetail( {
            graph: this.graph
        } );

        this.graph.render();

        this.query();

    },

    componentDidUpdate: function(prevProps, prevState) {
        if (prevState.spam != this.state.spam) {
            this.query();
        }
        if (prevState.blacklisted != this.state.blacklisted) {
            this.query();
        }
        if (prevState.bounce != this.state.bounce) {
            this.query();
        }
        if (prevState.timePicker != this.state.timePicker) {
            this.query();
        }

    },

    mapEmailSeries: function(series) {

        console.log(series);

        while (emailSeriesSpam.length > 0) {
            emailSeriesSpam.pop();
        }
        while (emailSeriesBlacklisted.length > 0) {
            emailSeriesBlacklisted.pop();
        }
        while (emailSeriesBounce.length > 0) {
            emailSeriesBounce.pop();
        }

        var shortest, shortestList;

        for (var property in series) {
            if (series.hasOwnProperty(property)) {
                if (typeof shortest == 'undefined') {
                    shortest = series[property].emails.buckets.length;
                    shortestList = series[property].emails.buckets;
                }
            }
            else if (series[property].emails.buckets.length < shortest) {
                shortest = series[property].emails.buckets.length;
                shortestList = series[property].emails.buckets;
            }
        }

        for (var serie in series) {
            if (series.hasOwnProperty(serie)) {
                for (i = 0; i < shortest; i++) {
                    var time = shortestList[i].key/1000;
                    var value = series[serie].emails.buckets[i].doc_count;

                    if (serie == 'spam') {
                        emailSeriesSpam.push({ x: time, y: value });
                    }
                    else if (serie == 'blacklisted') {
                        emailSeriesBlacklisted.push({ x: time, y: value });
                    }
                    else if (serie == 'bounce') {
                        emailSeriesBounce.push({ x: time, y: value });
                    }
                }
            }
        }


        for (i = 0; i < shortest; i++) {
            var time = shortestList[i].key/1000;
            var value = 0;
            if (emailSeriesSpam.length < shortest) {
                emailSeriesSpam.push({x: time, y: value})
            }
            if (emailSeriesBlacklisted.length < shortest) {
                emailSeriesBlacklisted.push({x: time, y: value})
            }
            if (emailSeriesBounce.length < shortest) {
                emailSeriesBounce.push({x: time, y: value})
            }
        }


        this.graph.update();

    },

    handleSearchChange: function() {
        var self = this;
        var value = this.refs.search.getValue();
        self.setState({
            searchValue: value
        });
    },

    search: function (e) {
        e.preventDefault();
        this.query();
    },

    handleRefreshChange: function () {
        var checked = this.refs.autorefresh.getChecked();
        this.setState({
            autorefresh: checked
        });
    },

    render: function() {

        var title = (
            <h3 className='panel-title'>Activity</h3>
        );

        return (
            <div className='panel panel-default'>
                <div className='panel-heading'>
                    {title}
                </div>
                <div className='panel-body'>
                    <Grid fluid={true}>
                        <Row>
                            <Col lg={2} xs={4}>
                                <form onSubmit={this.search}>
                                <Input
                                    type='text'
                                    value={this.state.searchValue}
                                    placeholder='Search emails...'
                                    label={false}
                                    ref='search'
                                    onChange={this.handleSearchChange} />
                                </form>

                                <div className="btn-group-vertical btn-group-vertical-justified margin-bottom" role="group">

                                    {this.props.types.map(function(item, i) {
                                        var typeClick = this.changeType.bind(this, item);
                                        return (
                                            <a type="button" key={i} className={this.state[item.toLowerCase()]==true ? 'btn btn-default active' : 'btn btn-default'} onClick={typeClick}>{item}</a>
                                        );
                                    }, this)}

                                </div>

                                <div className="btn-group-vertical btn-group-vertical-justified" role="group">

                                {this.props.timespans.map(function(item, i) {
                                    var timeClick = this.changeTimespan.bind(this, item[1]);
                                    return (
                                        <a type="button" key={item[1]} className={this.state.timePicker==item[1] ? 'btn btn-default active' : 'btn btn-default'} onClick={timeClick}>{item[0]}</a>
                                    );
                                }, this)}

                                </div>

                                <Input type="checkbox" label="Auto Refresh" onChange={this.handleRefreshChange} ref='autorefresh' />

                            </Col>
                            <Col lg={10} xs={8}>

                                <div id="emailgraph"></div>

                            </Col>
                        </Row>
                    </Grid>
                </div>
                <table className='table table-hover table-striped'>
                    <thead>
                        <tr>
                            <th>Timestamp</th>
                            <th>Sender</th>
                            <th>Recipient</th>
                            <th>Subject</th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.state.emails.map(function(email, index) {
                            return (
                                <ModalTrigger modal={<EmailModal payload={email['source']} />}>
                                <tr>
                                    <td>{email['Date']}</td>
                                    <td>{email['From']}</td>
                                    <td>{email['To']}</td>
                                    <td>{email['Subject']}</td>
                                </tr>
                                </ModalTrigger>
                            );
                        }, this)}
                    </tbody>
                </table>
            </div>
        );
    }

});

var EmailModal = React.createClass({
  render: function() {
    return (
        <Modal title="Email Payload" {...this.props} ref="modal" animation={false}>
          <div className="modal-body">
            <pre className="payload">
            {this.props.payload}
            </pre>
          </div>
          <div className="modal-footer">
          </div>
        </Modal>
      );
  }
});

module.exports = Graph;
