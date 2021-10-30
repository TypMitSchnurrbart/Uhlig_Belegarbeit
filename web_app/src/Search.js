const SearchBar = () => (
    <form action="./index.html" method ="get">
        <label htmlFor="header-search">
            <span className="visually-hidden">Gesetze: </span>
        </label>
        <input
            type="text"
            id="header-search"
            placeholder="Gesetze suchen"
            name="s"/>
        <button type="submit">suchen</button>
    </form>
);

export default SearchBar;
