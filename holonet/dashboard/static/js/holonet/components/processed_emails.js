/** @jsx React.DOM */

var React = require('react');
var request = require('superagent');
var cookie = require('cookie');


var mail_series = [];

var ProcessedEmails = React.createClass({

    getPayload: function() {
        return {
            "time_from": new Date().getTime()-604800000, //2419200000*6, // Minus one month
            "time_to": new Date().getTime()
        }
    },

    query: function() {
        var self = this;
        var cookies = cookie.parse(document.cookie);
        request
            .post('/api/processed/load/')
            .set('Accept', 'application/json')
            .set('X-CSRFToken', cookies['csrftoken'])
            .send(self.getPayload())
            .end(function(error, res){
                var response = res.body;

                self.mapEmailSeries(response.aggregations)

            });
    },

    componentDidMount: function () {

        this.palette = new Rickshaw.Color.Palette( { scheme: 'spectrum2000' } );

        this.graph = new Rickshaw.Graph( {
            element: document.querySelector("#processgraph"),
            renderer: 'bar',
            stack: false,
            height: '100',
            series: [{
                        data: mail_series,
                        color: this.palette.color(),
                        name: 'Processed Emails'
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

        this.interval = setInterval(this.reloadData, 10000);

    },

    mapEmailSeries: function(series) {

        while (mail_series.length > 0) {
            mail_series.pop();
        }

        var event_list = series['statistics']['processed']['buckets'];

        for (i = 0; i < event_list.length; i++) {
            var bucket_element = event_list[i];
            mail_series.push({x: bucket_element.key/1000, y: bucket_element.doc_count});
        }

        this.graph.update();

    },

    reloadData: function () {
        this.query();
    },

    render: function() {
        return (
            <div className='panel panel-default'>
                <div className='panel-heading'>
                    <h3 className='panel-title'>Processed Emails (LIVE)</h3>
                </div>
                <div className='panel-body'>
                    <div id="processgraph"></div>
                </div>
            </div>
        )
    }

});

module.exports = ProcessedEmails;
