import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import LoginForm from './components/auth/LoginForm';
import SignUpForm from './components/auth/SignUpModal/SignUpForm';
import NavBar from './components/NavBar';
import ProtectedRoute from './components/auth/ProtectedRoute';
import UsersList from './components/UsersList';
import { authenticate } from './store/session';
import Splash from './components/SplashPage/splash';
import Profile from './components/Profile';
import Feed from './components/Feed';

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async() => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>

      <Switch>
        <Route path='/' exact={true}>
          <Splash />
        </Route>
        <ProtectedRoute path='/feed' exact={true}>
          <NavBar />
          <Feed />
        </ProtectedRoute>
        {/* <Route path='/sign-up' exact={true}>
          <NavBar />
          <SignUpForm />
        </Route> */}
        <ProtectedRoute path='/users/:userId' exact={true} >
          <NavBar />
          <Profile />
        </ProtectedRoute>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
