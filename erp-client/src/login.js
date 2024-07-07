import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './login.css';
import logo from './SmartBoxERP.png';

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [showPassword, setShowPassword] = useState(false);
    const [token, setToken] = useState(null);
    const [error, setError] = useState(null);
    const [usernameError, setUsernameError] = useState('');
    const [passwordError, setPasswordError] = useState('');
    const [touchedFields, setTouchedFields] = useState({ username: false, password: false });

    const validateUsername = (username) => {
        if (username.length < 2 || username.length > 255) {
            return "Username must be between 2 and 255 characters.";
        }
        if (/[;'"\\]/.test(username)) {
            return "Username contains invalid characters.";
        }
        return '';
    };

    const validatePassword = (password) => {
        if (password.length < 8 || password.length > 255) {
            return "Password must be at least 8 characters long.";
        }
        if (!/\p{Ll}/u.test(password)) {
            return "Password must contain at least one lowercase letter.";
        }
        if (!/\p{Lu}/u.test(password)) {
            return "Password must contain at least one uppercase letter.";
        }
        return '';
    };

    const handleBlurUsername = () => {
        setTouchedFields({ ...touchedFields, username: true });
        setUsernameError(validateUsername(username));
    };

    const handleBlurPassword = () => {
        setTouchedFields({ ...touchedFields, password: true });
        setPasswordError(validatePassword(password));
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        setError(null);

        if (!usernameError && !passwordError) {
            try {
                const response = await axios.post('http://localhost:5000/login', { username, password });
                setToken(response.data.access_token);
                setError(null);
            } catch (error) {
                if (error.response && error.response.data) {
                    setError(error.response.data.error);
                } else {
                    setError("An unexpected error occurred.");
                }
            }
        }
    };

    useEffect(() => {
        if (touchedFields.username) setUsernameError(validateUsername(username));
        if (touchedFields.password) setPasswordError(validatePassword(password));
    }, [username, password]);

    return (
        <div className="login-container">
            <div className="logo">
                <img src={logo} alt="SmartBox ERP Logo" />
            </div>
            <form onSubmit={handleSubmit} className="form-container">
                <div className="input-field">
                    <input 
                        type="text" 
                        value={username} 
                        onChange={(e) => setUsername(e.target.value)} 
                        placeholder="Username"
                        className={usernameError ? 'input-error' : ''}
                        onBlur={handleBlurUsername}
                        title={usernameError ? usernameError : ''} 
                    />
                </div>
                <div className="input-field">
                    <input 
                        type={showPassword ? "text" : "password"} 
                        value={password} 
                        onChange={(e) => setPassword(e.target.value)} 
                        placeholder="Password" 
                        className={passwordError ? 'input-error' : ''}
                        onBlur={handleBlurPassword}
                        title={passwordError ? passwordError : ''}
                    />
                    <span
                        className="toggle-password"
                        onMouseDown={() => setShowPassword(true)} 
                        onMouseUp={() => setShowPassword(false)} 
                        onMouseLeave={() => setShowPassword(false)}
                    >
                        👁
                    </span>
                </div>
                <button type="submit" disabled={usernameError || passwordError}>Login</button>
            </form>
            {token && <div className="success">Authorization successful</div>}
            {error && <div className="error">{error}</div>}
        </div>
    );
};

export default Login;
