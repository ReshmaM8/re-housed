import logo from './trying again.png';
import './App.css';

function App() {
  return (
    <div className="App">

      <header className="App-header">
        <nav class="navBar">
          <div className="brandSection">
            <img src={logo} className="App-logo" alt="logo" />
            <h1 class = "brandName">Re-Housed</h1>
          </div>
          <ul>
            <li><a class = "underlineText" href="#">About</a></li>
            <li><a class= "underlineText" href="#">Design</a></li>
            <li><a class= "underlineText" href="#">Team</a></li>
            <button className="dashboardButton"> Dashboard </button>
          </ul>
        </nav>        
      </header>
      <main className="App-main">
        <section className="titleSection"> 
            <h1 className="title1">Mapping Tomorrow’s Shelters <i>Today.</i></h1>
            <h2 className="title2">Accelerating Shelter Selection through Data-Informed Decisions</h2>
          </section>
        <section className="statisticsSection">

        </section>
      </main>
    </div>
  );
}

export default App;
