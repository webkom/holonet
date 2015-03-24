/** @jsx React.DOM */

var React = require('react');
var ReactBootstrap = require('react-bootstrap');

var Grid = ReactBootstrap.Grid;
var BootstrapNavbar = ReactBootstrap.Navbar;
var Nav = ReactBootstrap.Nav;
var NavItem = ReactBootstrap.NavItem;

var FontAwsome = require('../fontawsome');

var Navbar = React.createClass({

    render: function() {
        return (
            <Grid fluid={true}>
                <BootstrapNavbar inverse={true} fluid={true}>
                    <div className="navbar-header">
                        <a className="navbar-brand" href="/">{this.props.brand}</a>
                    </div>
                    <Nav right={true}>
                        <NavItem href="/profile"><FontAwsome icon='user'/> User Profile</NavItem>
                        <NavItem href="/admin"><FontAwsome icon='cog'/> Admin</NavItem>
                        <NavItem href="/api"><FontAwsome icon='link'/> API</NavItem>
                        <NavItem href="/logout"><FontAwsome icon='power-off'/> Logout</NavItem>
                    </Nav>
                </BootstrapNavbar>
            </Grid>
        );
    }

});

module.exports = Navbar;
