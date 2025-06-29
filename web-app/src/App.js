import React, { useState } from "react";
import logo from './assets/trying again.png';
import mapE from './assets/etobicokeyork.png';
import mapN from './assets/northyork.png';
import mapS from './assets/scarbro.png';
import mapT from './assets/torontoeastyork.png';
import majda from './assets/majda.jpg';
import oorja from './assets/oorja.jpg';
import natalie from './assets/natalie.jpg';
import saba from './assets/saba.jpg';
import shaina from './assets/shaina.jpg';
import reshma from './assets/reshma.jpg';
import eptehal from './assets/eptehal.jpg';
import diana from './assets/diana.jpg';
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
  const teamMembers = [
    { id: 3, name: `Majda Lojpur`, image: majda },
    { id: 4, name: `Natalie Oulikhanian`, image: natalie},
    { id: 5, name: `Oorja Dorkar`, image: oorja },
    { id: 6, name: `Saba Memon`, image: saba},
    { id: 7, name: `Shaina Sumaiya`, image: shaina },
    { id: 8, name: `Reshma M`, image: reshma },
    { id: 1, name: `Mentor - Diana Moyano`, image: diana },
    { id: 2, name: `TA - Eptehal Nashnoush`, image: eptehal }
  ];

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
          <div className="statisticsgroup">
          <div className = "statisticsboth">
            <div className = "statistic1">
              <h2 className="statisticTitle">10,251</h2>
              <p className="statisticText">
                People actively homeless in the last three months.
              </p>
            </div >
            <div className = "statistic2">
              <h2 className="statisticTitle">385</h2>
              <p className="statisticText">
                Torontonians experienced being newly homeless in May 2025.
              </p>
            </div >
          </div>
          </div>


        </section>


      <section className="missionStatementSection">
      <div className="missionContainer">
        <h2 className="missionTitle">Mission Statement</h2>
        
        <p className="missionIntro">
          The Homelessness Services Capital Infrastructure Strategy (HSCIS) was 
          developed in response to the growing demands on Toronto's shelter 
          system, outlining six foundational goals to guide its framework:
        </p>

        <div className="goalsGrid">
          {/* Goal 1 */}
          <div className="goalItem">
            <div className="goalNumber">1</div>
            <div className="goalContent">
              <p>Plan Proactively and Prioritize Long-Term Infrastructure Needs</p>
            </div>
          </div>

          <div className="goalItem">
            <div className="goalNumber">2</div>
            <div className="goalContent">
              <p>Create Infrastructure that Fosters Dignity and Wellbeing</p>
            </div>
          </div>

          {/*foal 3 */}
          <div className="goalItem">
            <div className="goalNumber">3</div>
            <div className="goalContent">
              <p>Provide Resilient and Sustainable Infrastructure</p>
            </div>
          </div>

          {/* goal 4 */}
          <div className="goalItem">
            <div className="goalNumber">4</div>
            <div className="goalContent">
              <p>Strengthen Communications and Community Relationships</p>
            </div>
          </div>

          {/* goal 5 */}
          <div className="goalItem">
            <div className="goalNumber">5</div>
            <div className="goalContent">
              <p>Clarify Responsibilities, Authority and Decision Making</p>
            </div>
          </div>

          {/*goal 6 */}
          <div className="goalItem">
            <div className="goalNumber6">6</div>
            <div className="goalContent">
              <p>Strengthen the Collection, Management, and Analysis of Infrastructure Data</p>
            </div>
          </div>
        </div>

        <div className="missionIntro">
          <p>
            Re:Housed is grounded in the  <b>sixth goal → Strengthen the Collection, 
            Management, and Analysis of Infrastructure Data </b> —and builds on it by 
            leveraging publicly available datasets to develop an ethically informed, 
            data-driven AI model. Designed to support the City of Toronto's shelter site 
            planning and analysis, Re:Housed helps to make smarter, faster, and more 
            equitable infrastructure decisions.<br/>
            <br/>By anticipating future shelter demand through patterns in encampments 
            and service accessibility, the tool empowers planners to prioritize where 
            support is needed most—meeting people where they are, not just where 
            space happens to be available.
          </p>
        </div>

        <div className="missionButtons">
          <button className="hscisButton">
            <a href="https://www.toronto.ca/wp-content/uploads/2023/12/8c9e-HSCISinside231011spreadAODA.pdf">→ Read the HSCIS Report</a>
          </button>
          <button className="dashboardButton">
            Dashboard
          </button>
        </div>
      </div>

      <div className = "missionOutro">
        <nav className="outroNav">
          <div className="outro-item">
            <h3 className="outro-title">Fast Implementation</h3>
            <p className="outro-description">
              Re:Housed supports and accelerates site planning by helping identify high-need locations with data-backed urgency.
            </p>
          </div>

          <div className="outro-item">
            <h3 className="outro-title">Needs-Based Planning</h3>
            <p className="outro-description">
              Our model analyses where encampments are alongside nearby services like transit, wash rooms, and libraries to guide shelter placement that truly reflects need.
            </p>
          </div>

          <div className="outro-item">
            <h3 className="outro-title">Community-Center Impact</h3>
            <p className="outro-description">
              At the core of Re:Housed is empathy. Our approach prioritizes the lived realities of those experiencing homelessness
            </p>
          </div>
        </nav>
      </div>

    </section>

    <section className="TeamSection">
      <div className="team-container">
        <div className="team-content">
        <h1 className="missionTitle">
          Team
        </h1>
        
        <div className="team-grid">
          {teamMembers.map((member) => (
            <div key={member.id} className="team-member">
              {/* Circle Image */}
              <div className="member-image-container">
                <img 
                  src={member.image} 
                  className="member-image"
                />
              </div>
              
              {/* Name Placeholder */}
              <div className="member-info">
                <div className="member-name-placeholder">
                  {member.name}
                </div>
                <div className="member-title-placeholder"></div>
              </div>
            </div>
          ))}
        </div>
        </div>
      </div>
      </section>

  <div className="special-thanks-container">
        <section className="special-thanks-section">
          <h1 className="section-title">
            Special Thanks <span className="heart">💖</span>
          </h1>
          
          <p className="intro-text">
            A shout out to different people who helped to make this project:
          </p>
          
          <ul className="contributors-list">
            <li>Diana Moyano (Mentor)</li>
            <li>Eptehal Nashnoush (TA)</li>
            <li>Daniel (Vector)</li>
            <li>Micheal (TSS)</li>
            <li>Tia Aprile (MPAC)</li>
            <li>Michael Lyster (Director of Housing and Shelters, Homes First Society)</li>
            <li>Kiefer Shields (Property Services Supervisor at Shelter, Support & Housing Administration, The City of Toronto)</li>
            <li>Lorette Remanthin (Director of Infrastructure, Planning & Development (IPD), The City of Toronto - The Toronto Shelter & Support Services Division)</li>
            <li>Dina Lojpur (Pins production)</li>
          </ul>

          <div className="images-section">
            <h3 className="images-title">Our Stakeholders</h3>
            <div className="image-gallery">
              <div className="image-item">
                <img src="https://i0.wp.com/brentworks.ca/wp-content/uploads/2022/02/city-of-toronto-logo-vector-e1653754059472.png?ssl=1" alt="City of Toronto" />
                <p className="image-caption">City of Toronto</p>
              </div>
              <div className="image-item">
                <img src="https://kismetgroup.ca/wp-content/uploads/2017/08/MPAC-logo.png" alt="MPAC" />
                <p className="image-caption">MPAC</p>
              </div>
              <div className="image-item">
                <img src="https://mma.prnewswire.com/media/1011620/Vector_Institute_Vector_Institute_appoints_eight_new_Faculty_Mem.jpg?p=facebook" alt="Vector Institute" />
                <p className="image-caption">University of Toronto </p>
              </div>
            </div>
          </div>
        </section>

        <section className="land-acknowledgement-section">
          <h2 className="section-title">Land Acknowledgement</h2>
          
          <div className="acknowledgement-text">
            <p>
              We acknowledge the land we are meeting on is the traditional territory of many nations including the
              Mississaugas of the Credit, the Anishnabeg, the Chippewa, the Haudenosaunee and the Wendat peoples
              and is now home to many diverse First Nations, Inuit and Métis peoples. We also acknowledge that
              Toronto is covered by Treaty 13 with the Mississaugas of the Credit.
            </p>
          </div>
        </section>
      </div>

      </main>
    </div>
  );
}

export default App;