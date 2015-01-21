/** @jsx React.DOM */

var React = require('react');

var FontAwsome = React.createClass({

    render: function() {
        var classes = 'fa fa-' + this.props.icon;
        return (
            <i className={classes}></i>
            );
    }
});

module.exports = FontAwsome;
