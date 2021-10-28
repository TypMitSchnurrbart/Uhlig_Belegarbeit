import logo from './logo.svg';
import './App.css';
import SearchBar from './Search'
import myData from './Gesetze.json'

function App() {
  console.log(myData);
  return (
    <div className="App">
      <header className="App-header">
      <SearchBar />
      </header>
    </div>
  );
}
    
export default App;
