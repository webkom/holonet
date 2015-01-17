/** @jsx React.DOM */

var React = require('react');
var ReactBootstrap = require('react-bootstrap');
var request = require('superagent');
var cookie = require('cookie');


var Panel = ReactBootstrap.Panel;
var Input = ReactBootstrap.Input;
var ListGroup = ReactBootstrap.ListGroup;
var ListGroupItem = ReactBootstrap.ListGroupItem;

var LookupList = React.createClass({
    render: function() {
        var createItem = function(itemText) {
            var href = 'mailto:' + itemText;
            return <ListGroupItem><a href={href}>{itemText}</a></ListGroupItem>;
        };
        return <ListGroup>{this.props.items.map(createItem)}</ListGroup>;
    }
});

var Lookup = React.createClass({

    getInitialState: function() {
        return {
            value: '',
            items: []
        };
    },

    handleChange: function() {
        var self = this;
        var value = this.refs.lookup.getValue();
        self.setState({
            value: value
        });
        var cookies = cookie.parse(document.cookie);
        request
            .post('/api/lookup/lookup/')
            .set('Accept', 'application/json')
            .set('X-CSRFToken', cookies['csrftoken'])
            .send({
                email: value
            })
            .end(function(error, res){
                var response = res.body;
                var emails = response.map(function(data){
                    return data.email
                });
                self.setState({
                    items: emails
                });
            });
    },

    render: function() {

        var title = (
            <h3 className='panel-title'>Lookup</h3>
        );

        var footer = (
            <LookupList items={this.state.items} />
        );

        return (
            <div className='panel panel-default'>
                <div className='panel-heading'>
                    {title}
                </div>
                <div className='panel-body'>
                    <Input
                        type='text'
                        value={this.state.value}
                        placeholder='Enter email'
                        label={false}
                        ref='lookup'
                        groupClassName='no-padding no-margin'
                        onChange={this.handleChange} />
                </div>
                {footer}
            </div>
        );
    }

});

module.exports = Lookup;
