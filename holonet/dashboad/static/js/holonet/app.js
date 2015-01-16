/** @jsx React.DOM */

var React = require('react');

var growl = require('./components/growl.js');

var ReactBootstrap = require('react-bootstrap');
var Grid = ReactBootstrap.Grid;
var Row = ReactBootstrap.Row;

var Navbar = require('./components/navbar/navbar.js');
var ServiceStatus = require('./components/servicestatus.js');

var App = React.createClass({

    getInitialState: function() {
        var self = this;
        var connection = new Omnibus(
            SockJS,
            window.endpoint,
            {
                authToken: window.auth_token
            }
        );

        window.omnibus = connection;

        connection.on(Omnibus.events.CONNECTION_AUTHENTICATED, function(event) {
            var channel = connection.openChannel('holonet');
            console.log(channel);
            channel.on('notification', function(event) {
                var payload = event.data.payload;
                growl(payload.title, payload.message, payload.icon);
            });

            self.setState({
                channel: channel
            });
        });

        return {
            omnibus: connection
        };
    },

    render: function() {
        return (
            <div>
                <Navbar brand='Holonet'/>

                <Grid fluid={true}>
                    <Row>
                        <ServiceStatus service='elasticsearch' />
                        <ServiceStatus service='cache' />
                        <ServiceStatus service='celery' />
                        <ServiceStatus service='omnibus' />
                        <ServiceStatus service='policyservice' />
                        <ServiceStatus service='postfix' />
                    </Row>
                </Grid>

            </div>
        );
    }

});

React.render((
    <App/>
), document.getElementById('app'));
