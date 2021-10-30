import logo from './logo.svg';
import './App.css';
import SearchBar from './Search'
import laws from './laws.json'

function App() {
  const { search } = window.location;
  const query = new URLSearchParams(search).get('s');

  const matches = traverse_elements(json_elements(laws), query);
  const matched_laws = lookup_matches(matches, laws);
  var tablecontents;
  for (let i = 0; i < matches.length; i++){
    var entry = <tr>
      <td>{matches[i]}</td>
      <td>{matched_laws[i]["title"]}</td>
      <td>{matched_laws[i]["creationDate"]}</td>
      <td>{matched_laws[i]["foundingPlace"]}</td>
    </tr>;
    tablecontents += entry;    
  }
  var table = 
  <table>
    <tr>
      <th>Abkürzung</th>
      <th>Titel</th>
      <th>Ausarbeitungsdatum</th>
      <th>Fundstelle</th>    
    </tr>
    {tablecontent}
  </table>;

  return (
    <div className="App">
      <header className="App-header">
      <SearchBar />
        <ul>
        <p>{table}</p>
        <p>{build_table(matches)}</p>        
        </ul>
      </header>
    </div>
  );
}

function build_table(matches)
{
  let table = document.createElement("table");
  let thead = document.createElement("thead");
  let tbody = document.createElement("tbody");
  
  let header = document.createElement("tr");
  
  let heading_element1 = document.createElement("th");
  heading_element1.innerHTML="Abkürzung"

  let heading_element2 = document.createElement("th");
  heading_element1.innerHTML="Titel"

  let heading_element3 = document.createElement("th");
  heading_element1.innerHTML="Ausfertigungsdatum"

  let heading_element4 = document.createElement("th");
  heading_element1.innerHTML="Fundstelle"

  header.appendChild(heading_element1);
  header.appendChild(heading_element2);
  header.appendChild(heading_element3);
  header.appendChild(heading_element4);
  thead.appendChild(header);

  for(let i = 0; i<matches.length; i++)
  {
    let row = document.createElement("tr");
    let row_element1 = document.createElement("td");
    row_element1.innerHTML = matches[i];
    let row_element2 = document.createElement("td");
    row_element2.innerHTML = matches[i]["title"];
    let row_element3 = document.createElement("td");
    row_element3.innerHTML = matches[i]["creationDate"];
    let row_element4 = document.createElement("td");
    row_element4.innerHTML = matches[i]["foundingPlace"];

    row.appendChild(row_element1);
    row.appendChild(row_element2);
    row.appendChild(row_element3);
    row.appendChild(row_element4);

    tbody.appendChild(row);
  }
  table.appendChild(thead);
  table.appendChild(tbody);

  return table;

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
