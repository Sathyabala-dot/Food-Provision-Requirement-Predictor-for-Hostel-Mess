# Hostel Food Quantity Prediction System

A modern web application designed to reduce food wastage during festivals and holidays by predicting required food quantities for hostel students.

## Features

- **Interactive Form**: Collect all necessary data including festival name, date, student counts, meal type, and attendance percentage
- **Smart Calculations**: Automatically calculate food quantities based on expected attendees
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Clean UI**: Modern, professional interface suitable for academic projects and hackathons
- **Real-time Preview**: See predictions instantly after submitting the form

## Predicted Quantities

The system calculates the following quantities based on per-person consumption:

- **Rice**: 150g per person (for lunch/dinner)
- **Vegetables**: 200g per person
- **Cooking Oil**: 15ml per person
- **Dal/Lentils**: 100g per person (for lunch/dinner)
- **Chapati/Roti**: 2-3 pieces per person

## Technology Stack

- **React 18**: Modern JavaScript library for building user interfaces
- **TypeScript**: Type-safe JavaScript for better code quality
- **Tailwind CSS**: Utility-first CSS framework for styling
- **Vite**: Fast build tool and development server
- **Lucide React**: Beautiful, consistent icons

## How to Run

### Prerequisites

- Node.js (version 16 or higher)
- npm (comes with Node.js)

### Installation & Setup

1. **Install Dependencies**
   ```bash
   npm install
   ```

2. **Start Development Server**
   ```bash
   npm run dev
   ```

3. **Open in Browser**
   - The app will automatically open, or visit: http://localhost:5173
   - You should see the Hostel Food Quantity Prediction form

### Building for Production

To create an optimized production build:

```bash
npm run build
```

The built files will be in the `dist` folder.

### Preview Production Build

To preview the production build locally:

```bash
npm run preview
```

## How to Use the Application

1. **Enter Festival/Holiday Details**
   - Enter the name of the festival or holiday (e.g., Diwali, Christmas)
   - Select the date

2. **Enter Student Information**
   - Total number of students in the hostel
   - Number of vegetarian students
   - Number of non-vegetarian students

3. **Select Meal Type**
   - Choose between Breakfast, Lunch, or Dinner

4. **Set Expected Attendance**
   - Use the slider to set the expected attendance percentage
   - Default is 80%

5. **Calculate Prediction**
   - Click the "Calculate Prediction" button
   - View the predicted quantities for each food item

6. **Reset Form**
   - Click the "Reset" button to clear all inputs and start fresh

## Code Structure

```
src/
├── App.tsx          # Main application component with form and prediction logic
├── main.tsx         # Application entry point
├── index.css        # Global styles and Tailwind imports
└── vite-env.d.ts    # TypeScript declarations for Vite
```

## Key Components

### FormData Interface
Stores all input values from the form:
- Festival name
- Date
- Student counts (total, veg, non-veg)
- Meal type
- Attendance percentage

### PredictionResult Interface
Stores calculated food quantities:
- Rice (kg)
- Vegetables (kg)
- Oil (liters)
- Dal (kg)
- Chapati (pieces)
- Expected attendees count

### Calculation Logic

The prediction is calculated using simple per-person estimates:

```typescript
const expectedAttendees = (totalStudents × attendancePercentage) / 100
const quantity = expectedAttendees × perPersonAmount
```

## Customization

You can easily customize the per-person consumption rates in the `calculatePrediction` function:

```typescript
const ricePerPerson = 0.15;        // 150 grams
const vegetablesPerPerson = 0.2;   // 200 grams
const oilPerPerson = 0.015;        // 15 ml
const dalPerPerson = 0.1;          // 100 grams
const chapatiPerPerson = 3;        // 3 pieces
```

## Future Enhancements

- Add more food items (spices, desserts, beverages)
- Historical data tracking and analytics
- Export predictions to PDF/Excel
- Multi-language support
- Integration with inventory management
- Weather-based attendance predictions

## License

This project is open source and available for educational purposes.

## Support

For any questions or issues, please refer to the documentation or contact the development team.

---

**Note**: This is a frontend-only application. The calculations are performed on the client side using simple mathematical formulas. For production use, consider integrating with a backend API and machine learning models for more accurate predictions.
