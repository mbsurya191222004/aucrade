import { SignUp } from "../API/api.ts";
import { ChangeEvent, MouseEvent, useState } from "react";

export const Signup = () => {
  const [message, setMessage] = useState("");
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleChangeUsername = (e: ChangeEvent<HTMLInputElement>) => {
    setUsername(e.target.value);
  };

  const handleChangeEmail = (e: ChangeEvent<HTMLInputElement>) => {
    setEmail(e.target.value);
  };

  const handleChangePassword = (e: ChangeEvent<HTMLInputElement>) => {
    setPassword(e.target.value);
  };

  const handleClick = (e: MouseEvent<HTMLButtonElement, MouseEvent>) => {
    e.preventDefault();
    const response = SignUp(username, email, password);
    response
      .then((data) => {
        data.message
          ? setMessage(data.message)
          : data.username
          ? setMessage(data.username)
          : data.email
          ? setMessage(data.email)
          : setMessage(data.password);
      })
      .catch((error) => console.error(error));
  };

  return (
    <div>
      <label htmlFor="">{message}</label>
      <form id="SignUpForm">
        <input
          type="text"
          placeholder="username"
          id="username"
          onChange={(e) => handleChangeUsername(e)}
          value={username}
        />
        <input
          type="email"
          placeholder="email"
          id="email"
          onChange={(e) => handleChangeEmail(e)}
          value={email}
        />
        <input
          type="password"
          placeholder="password"
          id="password"
          onChange={(e) => handleChangePassword(e)}
          value={password}
        />
        <button onClick={(e) => handleClick(e)}>submit</button>
      </form>
    </div>
  );
};
