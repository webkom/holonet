/** @jsx React.DOM */

var React = require('react');

var Navbar = React.createClass({

    render: function() {
        return (
            <div className="container-fluid">
                <nav className="navbar navbar-default navbar-inverse" role="navigation">
                    <div className="container-fluid">
                        <div className="navbar-header">
                            <button type="button" className="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                                <span className="sr-only">Toggle navigation</span>
                                <span className="icon-bar"></span>
                                <span className="icon-bar"></span>
                                <span className="icon-bar"></span>
                            </button>
                            <a className="navbar-brand" href="/">{this.props.brand}</a>
                        </div>
                        <div className="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                            <ul className="nav navbar-nav">
                            </ul>
                            <ul className="nav navbar-nav navbar-right">
                                <li><a href="/logout"><i className="fa fa-power-off"></i> Logout</a></li>
                            </ul>
                        </div>
                    </div>
                </nav>
            </div>
        );
    }
});

module.exports = Navbar;
