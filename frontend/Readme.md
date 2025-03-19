# Frontend Documentation

## Overview
The frontend of this application is built using TypeScript and Vite. It is structured to facilitate modular development and maintainability.

## Project Structure
```
frontend/
│── auctry/
│   └── aucrade/
│       ├── src/               # Main source code
│       ├── public/            # Static assets
│       ├── index.html         # Entry HTML file
│       ├── package.json       # Project dependencies
│       ├── vite.config.ts     # Vite configuration
│       ├── tsconfig.json      # TypeScript configuration
│       └── README.md          # Project documentation
```

## Setup Instructions
1. Install Node.js (if not already installed).
2. Navigate to the frontend directory:
   ```sh
   cd frontend/auctry/aucrade
   ```
3. Install dependencies:
   ```sh
   npm install
   ```
4. Start the development server:
   ```sh
   npm run dev
   ```
5. Open the browser and visit `http://localhost:5173/` (or as specified in the terminal output).

## Development Guidelines
- **Component-Based Structure**: All UI components should be modular and reusable.
- **State Management**: If applicable, use a state management library.
- **Linting & Formatting**: Run `npm run lint` before committing code.
- **Build for Production**:
  ```sh
  npm run build
  ```
- **Environment Variables**: Use `.env` files for configuration.

## Key Files
- `src/main.tsx`: Entry point of the application.
- `src/App.tsx`: Main app component.
- `vite.config.ts`: Configuration for Vite.

## API Calls
The frontend interacts with the backend using the following API calls defined in `src/API/api.ts`:

### 1. **User Signup**
```ts
export const SignUp = async (username: string, email: string, password: string) => {
  const url = base_url + "/accounts/signup/";
  const response = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, email, password })
  });
  return response.json();
};
```
**Description**: Registers a new user with a username, email, and password.

### 2. **User Login**
```ts
export const LogIn = async (username: string, password: string) => {
  const url = base_url + "/accounts/login2/";
  const response = await fetch(url, {
    method: "POST",
    body: JSON.stringify({ username, password }),
    headers: { "Content-Type": "application/json" },
    credentials: "include"
  });
  return response.json();
};
```
**Description**: Logs in a user and maintains session cookies.

### 3. **Fetch All Items**
```ts
export const AllItems = async () => {
  const url = base_url + "/items/all/";
  const response = await fetch(url);
  return response.json();
};
```
**Description**: Retrieves a list of all available items.

Let me know if you need further explanations or modifications!

