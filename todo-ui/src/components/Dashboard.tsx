import React, { Component } from 'react';
import Login from './Login';

interface IProps {
}

interface IState {
}

class Dashboard extends Component<IProps, IState> {
    constructor(props: IProps) {
        super(props);
        this.state = {
        };
    }

    componentDidMount() {
    }

    componentWillMount() {
    }

    render() {
        return (
            <Login/>
        );
    }
}
export default Dashboard;
