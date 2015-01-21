/** @jsx React.DOM */

var React = require('react');
var ReactBootstrap = require('react-bootstrap');
var request = require('superagent');

var Panel = ReactBootstrap.Panel;

var SystemInformationList = React.createClass({

    render: function() {

        var createItem = function(item) {
            return (
                <tr>
                    <td>{item.title}</td>
                    <td>{item.value}</td>
                </tr>
            );
        };

        return (
            <table className='table'>
                <tbody>
                    {this.props.items.map(createItem)}
                </tbody>
            </table>
        )
    }

});

var SystemInformation = React.createClass({

    componentDidMount: function() {
        this.getInformation();
    },

    getInitialState: function() {
        return {
            items: []
        };
    },

    getInformation: function() {
        var self = this;
        request
            .get('/api/information/')
            .set('Accept', 'application/json')
            .end(function(error, res){
                var system_information = res.body;
                self.setState({
                    items: Object.keys(system_information).map(function(key, index) {

                        var value = system_information[key];

                        if (Array.isArray(value)) {

                            for (var innerValue in value) {
                                if (Array.isArray(value[innerValue])) {
                                    value[innerValue] = value[innerValue][0] + ' <' + value[innerValue][1] + '>'
                                }
                            }
                            value = value.join(', ')
                        }

                        return {
                            title: key,
                            value: value
                        }
                    })
                });
            });
    },

    render: function() {

        var title = (
            <h3 className='panel-title'>System Information</h3>
        );

        return (
            <div className='panel panel-default'>
                <div className='panel-heading'>
                    {title}
                </div>
                <SystemInformationList items={this.state.items} />
            </div>
        );
    }

});

module.exports = SystemInformation;
