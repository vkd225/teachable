import React, { Component } from 'react';
import RenderList from './RenderList';
import Container from '@material-ui/core/Container';

import { Redirect } from 'react-router-dom'
import * as HttpStatus from 'http-status-codes';

interface IProps {
    token: string;
}

interface IState {
    valid: boolean;
    lists: any;
}

class ListTask extends Component<IProps, IState> {  
    constructor(props: IProps) {
        super(props);
        this.componentDidMount = this.componentDidMount.bind(this);
        this.componentWillMount = this.componentWillMount.bind(this);
        this.getlist = this.getlist.bind(this);
        this.state = {
            valid: true,
            lists: [],
        };
    }

    async componentDidMount() {
    }

    async componentWillMount() {
        await this.getlist()
    }

    async getlist () {
        let url = 'https://xwyir2jma1.execute-api.us-east-1.amazonaws.com/prod/todos?function=get_lists&token=' 
        + this.props.token
        console.log('url: ', url)

        let result = await fetch(url, {
            method: 'GET'
        });

        // Bail if status code is not OK
        if ((result.status).toString() !== (HttpStatus.OK).toString()) return undefined;

        // Read response
        let response = await result.json();
             
        if (response.response === 'invalid token') {
            await this.setState({
                valid: false, 
            })
        } else {
            await this.setState({
                valid: true, 
                lists: response.response.lists
            })
        } 
    }

    render() {
        if (!this.state.valid) {
            return <Redirect to="/" />
        }
        return (
            <Container>
            <div style={{ marginTop: 50 }}>
                <h2>List of items</h2>
                <div style={{ margin : 30, marginTop: -10}}>
                    <RenderList data = {this.state.lists} token = {this.props.token}/>
                </div>
            </div>

            </Container>
        );
    }
}
export default ListTask;
