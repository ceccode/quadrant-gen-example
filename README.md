# Quadrant Chart Generator - Sample Flask app

A simple Flask web application that allows you to generate quadrant charts from CSV data using the [quadrant-gen library](https://pypi.org/project/quadrant-gen/0.2.0/)

## Features

- Upload CSV data directly in the browser
- Customize chart title and axis labels
- Generate charts in PNG or PDF format
- View charts in the browser or download them

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd quadrant-gen-example
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Testing the Installation

First, activate the virtual environment and run the test script:

```bash
source venv/bin/activate
python test_quadrant_gen.py
```

## Running the App

Activate the virtual environment and start the Flask app:

```bash
source venv/bin/activate
python app.py
```

Then open your browser to http://127.0.0.1:5001/

**Note**: Always activate the virtual environment before running any commands to ensure the correct dependencies are loaded.

## CSV Format

Your CSV data should have the following columns:
- `name`: Name of the data point
- `description`: Description of the data point (optional)
- `x`: X-coordinate (0.0 to 1.0)
- `y`: Y-coordinate (0.0 to 1.0)

Example:
```csv
name,description,x,y
Product A,High quality,0.2,0.8
Product B,Low cost,0.7,0.3
Product C,Innovative,0.8,0.7
Product D,Traditional,0.3,0.2
```

## Usage

1. Enter your CSV data in the text area
2. Set the chart title and axis labels
3. Choose the output format (PNG or PDF)
4. Click "Generate Chart" to view in the browser
5. Click "Generate & Download" to download the file

## Dependencies

- quadrant-gen==0.2.0 - Chart generation library
- Flask==2.3.3 - Web framework
- gunicorn==21.2.0 - WSGI server for production deployment
- matplotlib - Plotting library (required by quadrant-gen)

## Deployment to Render

This app is ready for deployment on [Render](https://render.com) (free tier available):

### Prerequisites
1. Push your code to a GitHub repository
2. Create a free Render account at https://render.com

### Deployment Steps
1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click **New** → **Web Service**
3. Connect your GitHub repository
4. Configure the service:
   - **Language**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Environment**: Select free tier

Your app will be live at `https://your-app-name.onrender.com` after deployment completes.

**Note**: Free tier sleeps after 15 minutes of inactivity and has 750 hours/month limit.
