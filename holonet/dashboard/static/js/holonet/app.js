/** @jsx React.DOM */

var React = require('react');

var ReactBootstrap = require('react-bootstrap');
var Grid = ReactBootstrap.Grid;
var Row = ReactBootstrap.Row;
var Col = ReactBootstrap.Col;

var Navbar = require('./components/navbar/navbar.js');
var ServiceStatus = require('./components/servicestatus.js');
var Lookup = require('./components/lookup.js');
var ReverseLookup = require('./components/lookupreverse.js');
var SystemInformation = require('./components/systeminformation.js');
var Graph = require('./components/graph.js');
var ProcessedEmails = require('./components/processed_emails.js');

var App = React.createClass({

    render: function() {
        return (
            <div>
                <Navbar brand='Holonet'/>

                <Grid fluid={true}>
                    <Row>
                        <ServiceStatus service='postfix' />
                        <ServiceStatus service='policyservice' />
                        <ServiceStatus service='saslservice' />
                        <ServiceStatus service='elasticsearch' />
                        <ServiceStatus service='cache' />
                        <ServiceStatus service='celery' />
                    </Row>
                </Grid>

                <Grid fluid={true}>
                    <Row>
                        <Col lg={3} md={4}>
                            <Lookup/>
                            <ReverseLookup/>
                            <SystemInformation/>
                        </Col>
                        <Col lg={9} md={8}>
                            <ProcessedEmails/>
                        </Col>
                        <Col lg={9} md={8}>
                            <Graph/>
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
