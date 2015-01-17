/** @jsx React.DOM */

var React = require('react');

var growl = require('./components/growl.js');

var ReactBootstrap = require('react-bootstrap');
var Grid = ReactBootstrap.Grid;
var Row = ReactBootstrap.Row;
var Col = ReactBootstrap.Col;

var Navbar = require('./components/navbar/navbar.js');
var ServiceStatus = require('./components/servicestatus.js');
var Lookup = require('./components/lookup.js');
var ReverseLookup = require('./components/lookupreverse.js');
var SystemInformation = require('./components/systeminformation.js');

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
                        <ServiceStatus service='websockets' />
                        <ServiceStatus service='policyservice' />
                        <ServiceStatus service='postfix' />
                    </Row>
                </Grid>

                <Grid fluid={true}>
                    <Row>
                        <Col lg={3} md={4}>
                            <Lookup/>
                            <ReverseLookup/>
                            <SystemInformation/>
                        </Col>
                    </Row>
                </Grid>

            </div>
        );
    }

});

React.render((
    <App/>
), document.getElementById('app'));
