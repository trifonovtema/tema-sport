import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import PenaltyInput from './components/PenaltyInput';
import Results from './pages/Results';
import Home from './pages/Home';
import GeneratePDF from './pages/GeneratePDF';
import InputTiming from './pages/InputTiming';

const App = () => {
  return (
    <Router>
      <div>
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/penalties" component={PenaltyInput} />
//          <Route path="/results" component={Results} />
          <Route path="/generate-pdf" component={GeneratePDF} />
          <Route path="/timing" component={InputTiming} />
        </Switch>
      </div>
    </Router>
  );
};

export default App;
