import React, { Component } from 'react';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';

interface IProps {
}

interface IState {
}

const baseurl = 'https://822qpk33pk.execute-api.us-east-1.amazonaws.com/prod/rimsconference?warehouse_id='
class Login extends Component<IProps, IState> {

    
    constructor(props: IProps) {
        super(props);
        this.componentDidMount = this.componentDidMount.bind(this);
        this.state = {
        };
    }

    componentDidMount() {
    }

    componentWillMount() {
    }


    render() {
        return (
            <Container maxWidth="xs">
            <div>
                <Typography component="h1" variant="h5">
                    Sign in
                </Typography>
                <form noValidate>
                <TextField
                    variant="outlined" margin="normal"
                    required
                    fullWidth
                    id="email"
                    label="Email Address"
                    name="email"
                    autoComplete="email"
                    autoFocus
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
                    autoComplete="current-password"
                />
                
                <Button
                    type="submit"
                    fullWidth
                    variant="contained"
                    color="primary"
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
