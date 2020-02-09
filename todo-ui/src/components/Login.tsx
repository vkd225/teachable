import React, { Component } from 'react';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';

import * as HttpStatus from 'http-status-codes';

interface IProps {
}

interface IState {
    username: string;
    password: string;
}

class Login extends Component<IProps, IState> {  
    constructor(props: IProps) {
        super(props);
        this.componentDidMount = this.componentDidMount.bind(this);
        this.login = this.login.bind(this);
        this.getToken = this.getToken.bind(this);
        this.state = {
            username: '',
            password: '',
        };
    }

    componentDidMount() {
    }

    componentWillMount() {
    }


    async login() {
        this.setState({
            username: this.state.username, 
            password: this.state.password
        })
        console.log('user: ', this.state.username)
        console.log('pass: ', this.state.password)
        let url = 'https://xwyir2jma1.execute-api.us-east-1.amazonaws.com/prod/todos?function=login&username=' + 
            this.state.username + '&passwor=' + this.state.password

        await this.getToken(url)
    }

    async getToken (url: string) {
        try {
            let result = await fetch(url, {
                method: 'GET',
            });

            // Bail if status code is not OK
            if ((result.status).toString() !== (HttpStatus.OK).toString()) return undefined;

            console.log('result type: ', result.type)
            // Read response
            let response = await result.json();
            console.log('res json: ', response)
            return response;

        } catch (error) 
        {
            return undefined;
        }
    }

    render() {
        return (
            <Container maxWidth="xs">
            <div style={{ marginTop: 50 }}>
                <Typography component="h1" variant="h5">
                    Sign in
                </Typography>
                <form>
                    <TextField
                        variant="outlined" 
                        margin="normal"
                        required
                        fullWidth
                        id="username"
                        label="Username"
                        name="username"
                        autoFocus
                        value={this.state.username}
                        onChange={e => this.setState({ username: e.target.value })}
                    />
                    <TextField
                        variant="outlined" 
                        margin="normal"
                        required
                        fullWidth
                        name="password"
                        label="Password"
                        type="password"
                        id="password"
                        onChange={e => this.setState({ password: e.target.value })}
                    />
                
                    <Button
                        fullWidth
                        variant="contained"
                        color="primary"
                        onClick={this.login}
                    >
                        Sign In
                    </Button>
                </form>
            </div>
            </Container>
        );
    }
}
export default Login;
