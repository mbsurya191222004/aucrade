const base_url = "https://aucrade.onrender.com";

export const SignUp = async (
  username: string | undefined,
  email: string | undefined,
  password: string | undefined
) => {
  const url = base_url + "/accounts/signup/";
  const response = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      username: username,
      password: password,
      email: email,
    }),
  });
  const data = await response.json();
  if (response.ok) {
    return data;
  }
  return data;
};

export const LogIn = async (
  username: string,

  password: string
) => {
  const url = base_url + "/accounts/login2/";
  const response = await fetch(url, {
    method: "POST",
    body: JSON.stringify({ username, password }),
    headers: { "Content-Type": "application/json" },
    credentials: "include", // Allows browser to store and send cookies
  });

  const data = await response.json();
  return data;
};

export const AllItems = async () => {
  const url = base_url + "/auction/allitems";
  const response = await fetch(url, {
    method: "GET",
    headers: { "Content-Type": "application/json" },
    credentials: "include",
  });
  const data = await response.json();
  return data;
};
