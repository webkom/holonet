/** @jsx React.DOM */

var React = require('react');
var ReactBootstrap = require('react-bootstrap');
var request = require('superagent');

var Col = ReactBootstrap.Col;

var ServiceStatus = React.createClass({

    getInitialState: function() {
        return {
            status: 0
        };
    },

    getDefaultProps: function() {
      return {
        width: 2,
          small: 4
      };
    },

    componentDidMount: function() {
        this.getStatus();
        this.interval = setInterval(this.getStatus, 10000);
    },

    getStatus: function() {
        var self = this;
        request
            .get('/api/status/' + self.props.service + '/')
            .set('Accept', 'application/json')
            .end(function(error, res){
                var service_status = res.body.status;
                self.setState({
                    status: service_status
                });
            });
    },

    render: function() {
        return (
            <Col lg={this.props.width} sm={this.props.small}>
                <div className={this.state.status==0 ? 'panel panel-primary status-panel not-responding' : 'panel panel-primary status-panel'}>
                    <div className="panel-heading">
                        <div className="row">
                            <div className="col-xs-12 text-center">
                                <div className="huge">{this.state.status==0 ? 'Not Running' : 'Running'}</div>
                                <div>{this.props.service}</div>
                            </div>
                        </div>
                    </div>
                </div>
            </Col>
        );
    }

});

module.exports = ServiceStatus;
