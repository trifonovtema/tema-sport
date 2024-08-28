import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import PenaltyInput from "./components/PenaltyInput";

const App = () => {
  return (
    <Router>
      <div>
        <Switch>
          <Route path="/penalties" component={PenaltyInput} />
        </Switch>
      </div>
    </Router>
  );
};

export default App;
