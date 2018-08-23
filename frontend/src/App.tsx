import axios from 'axios';
import * as React from 'react';

export interface ILoginFormState {
  userName: string;
  password: string;
  email: string;
  phoneNo: string;
}

export class LoginForm extends React.PureComponent<{}, ILoginFormState> {
  constructor(props: {}) {
    super(props);
    this.state = { userName: '', password: '', email: '', phoneNo: '' }
  }

  public handleSubmit = (e) => {
    e.preventDefault();
    const { userName, password, email, phoneNo } = this.state;
    axios.post('http://localhost:8000/SaveUser', {
      email, phoneNo, password, userName
    }).then((response) => {
      console.log(response);
    })
  }

  public render() {
    return <div>
      <form onSubmit={this.handleSubmit} >
        <label>Username:</label>
        <input onChange={e => this.setState({ userName: e.target.value })} />
        <label>Password:</label>
        <input onChange={e => this.setState({ password: e.target.value })} />
        <label>Email::</label>
        <input onChange={e => this.setState({ email: e.target.value })} />
        <label>Phone No.:</label>
        <input onChange={e => this.setState({ phoneNo: e.target.value })} />
        <button>Submit</button>
      </form>
    </div>
  }
}
