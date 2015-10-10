import { Component, PropTypes } from 'react';

export default class Wrapper extends Component {

  static propTypes = {
    dispatch: PropTypes.func.isRequired
  };

  render() {
    return this.props.children;
  }
}
