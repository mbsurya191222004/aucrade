import { LogIn } from "../API/api.ts";
import { ChangeEvent, MouseEvent, useState } from "react";

export const Login = () => {
  const [message, setMessage] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleChangeUsername = (e: ChangeEvent<HTMLInputElement>) => {
    setUsername(e.target.value);
  };

  const handleChangePassword = (e: ChangeEvent<HTMLInputElement>) => {
    setPassword(e.target.value);
  };

  const handleClick = (e: MouseEvent<HTMLButtonElement, MouseEvent>) => {
    e.preventDefault();
    const response = LogIn(username, password);
    response
      .then((data) => {
        setMessage(`${data.access}`);
      })
      .catch((error) => console.error(error));
  };

  return (
    <div>
      <form id="SignUpForm">
        <input
          type="text"
          placeholder="username"
          id="username"
          onChange={(e) => handleChangeUsername(e)}
          value={username}
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
