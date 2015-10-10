import React, { Component, PropTypes } from 'react';
import { connect } from 'react-redux';
import Wrapper from '../components/wrapper';

@connect(state => ({
  dispatch: state.dispatch
}))
export default class AppContainer extends Component {

  static propTypes = {
    dispatch: PropTypes.func.isRequired
  };

  render() {
    return <Wrapper {...this.props} />;
  }

}
