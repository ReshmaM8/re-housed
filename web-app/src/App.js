import React, { useState } from "react";
import logo from './assets/trying again.png';
import mapE from './assets/etobicokeyork.png';
import mapN from './assets/northyork.png';
import mapS from './assets/scarbro.png';
import mapT from './assets/torontoeastyork.png';
import './App.css';

function App() {
  const [tooltip, setTooltip] = useState(null);
  const [mousePosition, setMousePosition] = useState({ x: 0, y: 0 });

  const showTooltip = (region, event) => {
    setTooltip(region);
    setMousePosition({ x: event.clientX, y: event.clientY });
  };

  const hideTooltip = () => {
    setTooltip(null);
  };

  const updateMousePosition = (event) => {
    setMousePosition({ x: event.clientX, y: event.clientY });
  };

  const getTooltipContent = (region) => {
    const tooltipData = {
      'north-york': {
        title: 'North York',
        info: '13% of Total Homeless Pop. (944 people)'
      },
      'scarborough': {
        title: 'Scarborough',
        info: '21% of Total Homeless Pop. (1387 people)'
      },
      'toronto-east-york': {
        title: 'Toronto & East York',
        info: '51% of Total Homeless Pop. (3332 people)'
      },
      'etobicoke-york': {
        title: 'Etobicoke York',
        info: '15% of Total Homeless Pop. (980 people)'
      }
    };
    return tooltipData[region] || { title: 'Unknown Region', info: 'No data available' };
  };

  return (
    <div className="App">
      <header className="App-header">
        <nav className="navBar">
          <div className="brandSection">
            <img src={logo} className="App-logo" alt="logo" />
            <h1 className="brandName">Re-Housed</h1>
          </div>


          <ul>
            <li><a className="underlineText" href="#">About</a></li>
            <li><a className="underlineText" href="#">Design</a></li>
            <li><a className="underlineText" href="#">Team</a></li>
            <button className="dashboardButton">Dashboard</button>
          </ul>
        </nav>        
      </header>
      
      <main className="App-main">
        <section className="titleSection"> 
          <h1 className="title1">Mapping Tomorrow's Shelters <i>Today.</i></h1>
          <h2 className="title2">Accelerating Shelter Selection through Data-Informed Decisions</h2>
        </section>
        
        <section className="statisticsSection">
          <div className="map-container">
            <div 
              className="map-section north-york" 
              onMouseEnter={(e) => showTooltip('north-york', e)}
              onMouseMove={updateMousePosition}
              onMouseLeave={hideTooltip}
            >
              <img src={mapN} className="map-piece" alt="North York" />
            </div>
            
            <div 
              className="map-section etobicoke-york" 
              onMouseEnter={(e) => showTooltip('etobicoke-york', e)}
              onMouseMove={updateMousePosition}
              onMouseLeave={hideTooltip}
            >
              <img src={mapE} className="map-piece" alt="Etobicoke York" />
            </div>
            
            <div 
              className="map-section toronto-east-york" 
              onMouseEnter={(e) => showTooltip('toronto-east-york', e)}
              onMouseMove={updateMousePosition}
              onMouseLeave={hideTooltip}
            >
              <img src={mapT} className="map-piece" alt="Toronto & East York" />
            </div>
            
            <div 
              className="map-section scarborough" 
              onMouseEnter={(e) => showTooltip('scarborough', e)}
              onMouseMove={updateMousePosition}
              onMouseLeave={hideTooltip}
            >
              <img src={mapS} className="map-piece" alt="Scarborough" />
            </div>

                      <div className="map-caption">
            <p className="mapCaptionText">Hover over a region to see its homeless population statistics.</p>
          </div>
            
          </div>


          {tooltip && (
            <div 
              className="tooltip" 
              style={{
                left: mousePosition.x,
                top: mousePosition.y
              }}
            >
              <strong>{getTooltipContent(tooltip).title}</strong>
              <br />
              {getTooltipContent(tooltip).info}
            </div>
          )}

        </section>
      </main>
    </div>
  );
}

export default App;