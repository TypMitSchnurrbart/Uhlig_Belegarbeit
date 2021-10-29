import logo from './logo.svg';
import './App.css';
import SearchBar from './Search'
import laws from './laws.json'

function App() {
  const { search } = window.location;
  const query = new URLSearchParams(search).get('s');

  const matches = traverse_elements(json_elements(laws), query);
  const matched_laws = lookup_matches(matches, laws);
  var text = "";
  for (let i = 0; i < matches.length; i++){
        text += matches[i];
        text += matched_laws[i]["title"];
        text += matched_laws[i]["creationDate"];
        text += matched_laws[i]["foundingPlace"];
  }
  return (
    <div className="App">
      <header className="App-header">
      <SearchBar />
        <ul>
        <p>{text}</p>
        </ul>
      </header>
    </div>
  );
}

function json_elements(jsonObj){
    var keys = Object.keys(jsonObj);
    return keys
}

function traverse_elements(keys, query){
    var acc = [];
    keys.forEach(function(key){
        if (key.includes(query)){
            acc.push(key);
            console.log(key);
        }
});
    return acc;
}

function lookup_matches(matches, laws){
    var acc = []
    matches.forEach(function(key){
        console.log(laws[key]);
        acc.push(laws[key]);
    });
    return acc;
}


export default App;
