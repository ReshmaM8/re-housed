import streamlit as st
#import plotly.express as px
import pandas as pd
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Re:Housed",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)


st.markdown("""
<style>
    /* Hide Streamlit's default header and footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    body {
        background-color: #EAEDF6; /* light grey-blue */
    }
    /* Custom header styling */
    .custom-header {
        background: #EAEDF6;
        padding: 1rem 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 0;
    }
    
    .logo-section {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .logo-icon {
        width: 100px;
        height: 100px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
    }
    
    .nav-links {
        display: flex;
        gap: 2rem;
        align-items: center;
    }
    
    .nav-link {
        color: #1264AB;
        text-decoration: none;
        font-weight: 500
        font-size: 1.8em;
    }
    
    .dashboard-btn {
        background: #4A90E2;
        color: white;
        padding: 0.5rem 1.5rem;
        border-radius: 20px;
        border: none;
        font-weight: 500;
        cursor: pointer;
    }
    

    .title {
        background: #EAEDF6; 
        padding: 4rem 2rem;
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .Main-title {
        color: #1264AB;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    
    .subtitle {
        font-size: 1.2rem;
        color: #1264AB;
        margin-bottom: 3rem;
    }
    
    /* Statistics cards */
    .stats-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        gap: 4rem;
        margin: 2rem 0;
    }
    
    .stat-card {
        text-align: center;
        background: #EAEDF6;
        padding: 2rem;
        min-width: 200px;
    }
    
    .stat-number {
        font-size: 3rem;
        font-weight: bold;
        color: #0CCE6B;
        margin-bottom: 0.5rem;
    }
    
    .stat-description {
        color: #666;
        font-size: 1.2rem;
        line-height: 1.4;
        width: 80%;
    }
    

    .mission-section {
        background: #EAEDF6;
        padding: 4rem 2rem;
        text-align: center;
    }
    
    .section-title {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1264AB;
        margin-bottom: 2rem;
    }
    
    .mission-text {
        font-size: 1.1rem;
        line-height: 1.6;
        color: black;
    }
    
    /* Design process section */
    .design-section {
        background: #f8f9fa;
        padding: 4rem 2rem;
        text-align: center;
    }
    
    .process-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        margin: 2rem auto;
        max-width: 800px;
    }
    
    .r-icon {
        width: 60px;
        height: 60px;
        background: #e74c3c;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 2rem;
        font-weight: bold;
        margin: 0 auto 2rem auto;
    }
    
    /* Team section */
    .team-section {
        background: white;
        padding: 4rem 2rem;
        text-align: center;
    }
    
    .team-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
        gap: 2rem;
        max-width: 600px;
        margin: 2rem auto;
    }
    
    .team-member {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    
    .avatar {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        margin-bottom: 1rem;
    }
    
    /* Special mentions */
    .special-section {
        background: #f8f9fa;
        padding: 2rem;
        text-align: center;
    }
    
    /* Buttons */
    .action-btn {
        background: #4A90E2;
        color: white;
        padding: 0.8rem 2rem;
        border-radius: 25px;
        border: none;
        font-weight: 500;
        margin: 1rem;
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
    }
    
    .secondary-btn {
        background: transparent;
        color: #4A90E2;
        border: 2px solid #4A90E2;
    }
</style>
""", unsafe_allow_html=True)

def create_header():
    st.markdown('<div class="custom-header">',unsafe_allow_html=True )

    logo = Image.open('app/images/logo.png')
    st.image(logo, width=60)

    st.markdown("""
            <h2 style="margin: 0; color: #1264AB;">Re:Housed</h2>
        <div class="nav-links">
            <a href="#" class="nav-link">About</a>
            <a href="#" class="nav-link">Design</a>
            <a href="#" class="nav-link">Team</a>
            <button class="dashboard-btn">Dashboard</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

def title_section():
    st.markdown("""
    <div class="title">
        <h1 color: #1264AB class="Main-title">Mapping Tomorrow's Shelters <i>Today.</i></h1>
        <p class="subtitle">Accelerating Shelter Selection through Data-Informed Decisions</p>
    </div>
        <div class="stats-container">
            <div class="stat-card">
                <div class="stat-number">10,418</div>
                <div class="stat-description">
                    is the current total number of homeless people in Toronto, 
                    with the highest cited reason being "lack of affordable housing"
                </div>
            </div>
            <div class="stat-card">
                <div class="stat-number">385</div>
                <div class="stat-description">
                    Torontonians experienced being newly homeless in May 2025*
                </div>
            </div>
        </div>
 
    """, unsafe_allow_html=True)

def create_mission_section():
    st.markdown("""
    <div class="mission-section">
        <h2 class="section-title">Mission Statement</h2>
        <div class="mission-text">
            <p>The Homelessness Services Capital Infrastructure Strategy (HSCIS) was developed in response to the growing demands on Toronto's shelter system, outlining six foundational goals to guide its framework:</p>
            <p style="margin-top: 2rem;">Re:Housed is grounded in the sixth goal—Strengthen the Collection, Management, Analysis of Infrastructure Data—and builds on it by leveraging publicly available datasets to develop an ethically informed, data-driven AI model. Designed to support TFN of Toronto's shelter site planning and analysis, Re:Housed helps to make smarter, faster, and more equitable infrastructure decisions.</p>
            <p style="margin-top: 2rem;">By anticipating future shelter demand through patterns in encampments and service accessibility, the tool empowers planners to prioritize where support is needed—meeting people where they are, not just where space happens to be available.</p>
        </div>
        
    </div>
    """, unsafe_allow_html=True)

def create_design_section():
    st.markdown("""
    <div class="design-section">
        <h2 class="section-title">Design Process</h2>
        
        <div class="process-card">
            <div class="r-icon">R</div>
            <p style="text-align: left; line-height: 1.6;">
                Our project followed a structured three-week development cycle: ideation, model development, and application building. We began with the core objective of addressing existing gaps in current decision-making processes, working collaboratively to refine our scope and features with guidance from our mentor, Diane, and TA, Epithet. During the ideation phase, we conducted a stakeholder analysis and reviewed municipal policies, assessing both opportunities for innovation and acknowledging existing systemic constraints, and the values driving public and institutional decision-making. We then engaged in interviews with subject-matter experts and community stakeholders to validate our assumptions, identify key user groups, and better understand the complex challenges. Using publicly available datasets, we conducted exploratory data analysis (EDA) to extract meaningful patterns and insights. This iterative discovery process informed our identification of key pain points, data requirements, feature engineering priorities, and model selection strategy—ultimately culminating in our final solution remains aligned with both user needs and project feasibility.
            </p>
            
            <div style="margin-top: 2rem;">
                <a href="#" class="action-btn">📖 Read our report</a>
                <a href="#" class="action-btn secondary-btn">Dashboard</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_team_section():
    st.markdown("""
    <div class="team-section">
        <h2 class="section-title">Team</h2>
        
        <div class="team-grid">
            <div class="team-member">
                <div class="avatar" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);"></div>
            </div>
            <div class="team-member">
                <div class="avatar" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);"></div>
            </div>
            <div class="team-member">
                <div class="avatar" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);"></div>
            </div>
            <div class="team-member">
                <div class="avatar" style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);"></div>
            </div>
            <div class="team-member">
                <div class="avatar" style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);"></div>
            </div>
            <div class="team-member">
                <div class="avatar" style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);"></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_special_mentions():
    st.markdown("""
    <div class="special-section">
        <h2 class="section-title">Special Mentions <3</h2>
    </div>
    """, unsafe_allow_html=True)

# Main app
def main():
    create_header()
    title_section()
    create_mission_section()
    create_design_section()
    create_team_section()
    create_special_mentions()

main()