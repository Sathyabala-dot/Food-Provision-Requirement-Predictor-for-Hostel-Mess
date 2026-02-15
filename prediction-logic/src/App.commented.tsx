/**
 * HOSTEL FOOD QUANTITY PREDICTION SYSTEM
 *
 * This application helps hostel administrators predict required food quantities
 * during festivals and holidays to reduce food wastage.
 *
 * Key Features:
 * - Collects student data and meal preferences
 * - Calculates food quantities based on attendance percentage
 * - Displays predictions in an easy-to-read format
 */

import { useState } from 'react';
import { Utensils, Calendar, Users, Calculator } from 'lucide-react';

// Interface to define the structure of form input data
interface FormData {
  festivalName: string;         // Name of the festival or holiday
  date: string;                 // Date of the event
  totalStudents: number;        // Total number of students in hostel
  vegStudents: number;          // Number of vegetarian students
  nonVegStudents: number;       // Number of non-vegetarian students
  mealType: string;             // Type of meal: Breakfast, Lunch, or Dinner
  attendancePercentage: number; // Expected attendance as a percentage
}

// Interface to define the structure of prediction results
interface PredictionResult {
  rice: number;           // Predicted rice quantity in kg
  vegetables: number;     // Predicted vegetables quantity in kg
  oil: number;           // Predicted oil quantity in liters
  dal: number;           // Predicted dal/lentils quantity in kg
  chapati: number;       // Predicted chapati count
  expectedAttendees: number; // Calculated number of expected attendees
}

function App() {
  // State to store form data - initialized with default values
  const [formData, setFormData] = useState<FormData>({
    festivalName: '',
    date: '',
    totalStudents: 0,
    vegStudents: 0,
    nonVegStudents: 0,
    mealType: 'Lunch',              // Default meal type is Lunch
    attendancePercentage: 80,       // Default attendance is 80%
  });

  // State to store prediction results
  const [prediction, setPrediction] = useState<PredictionResult | null>(null);

  // State to control visibility of results section
  const [showResults, setShowResults] = useState(false);

  /**
   * Handle input changes from form fields
   * Updates the formData state whenever user types or selects something
   */
  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      // Convert to number for numeric fields, keep as string for text fields
      [name]: name === 'festivalName' || name === 'date' || name === 'mealType' ? value : Number(value),
    }));
  };

  /**
   * Calculate food quantity predictions
   * This is the core logic that computes how much food is needed
   */
  const calculatePrediction = (e: React.FormEvent) => {
    e.preventDefault(); // Prevent form from reloading the page

    // STEP 1: Calculate expected number of attendees
    // Formula: (Total Students × Attendance %) / 100
    const expectedAttendees = Math.round((formData.totalStudents * formData.attendancePercentage) / 100);

    // STEP 2: Define per-person consumption rates (in kg or liters)
    // These values are based on typical Indian meal portions
    const ricePerPerson = formData.mealType === 'Breakfast' ? 0 : 0.15;      // 150g, not needed for breakfast
    const vegetablesPerPerson = 0.2;                                          // 200g
    const oilPerPerson = 0.015;                                               // 15ml
    const dalPerPerson = formData.mealType === 'Breakfast' ? 0 : 0.1;        // 100g, not needed for breakfast
    const chapatiPerPerson = formData.mealType === 'Breakfast' ? 2 : 3;     // 2 for breakfast, 3 for lunch/dinner

    // STEP 3: Calculate total quantities by multiplying per-person rates with attendee count
    // Math.ceil rounds up to ensure we have enough food
    const result: PredictionResult = {
      rice: Math.ceil(expectedAttendees * ricePerPerson * 10) / 10,           // Round to 1 decimal place
      vegetables: Math.ceil(expectedAttendees * vegetablesPerPerson * 10) / 10,
      oil: Math.ceil(expectedAttendees * oilPerPerson * 100) / 100,           // Round to 2 decimal places
      dal: Math.ceil(expectedAttendees * dalPerPerson * 10) / 10,
      chapati: Math.ceil(expectedAttendees * chapatiPerPerson),               // Round to whole number
      expectedAttendees,
    };

    // STEP 4: Update state to display results
    setPrediction(result);
    setShowResults(true);
  };

  /**
   * Reset form to initial state
   * Clears all inputs and hides results
   */
  const handleReset = () => {
    setFormData({
      festivalName: '',
      date: '',
      totalStudents: 0,
      vegStudents: 0,
      nonVegStudents: 0,
      mealType: 'Lunch',
      attendancePercentage: 80,
    });
    setPrediction(null);
    setShowResults(false);
  };

  // RENDER: The UI of the application
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-50 py-8 px-4">
      <div className="max-w-4xl mx-auto">

        {/* HEADER SECTION */}
        <header className="text-center mb-8">
          <div className="flex items-center justify-center gap-3 mb-3">
            <Utensils className="w-10 h-10 text-blue-600" />
            <h1 className="text-4xl font-bold text-gray-800">Hostel Food Quantity Prediction</h1>
          </div>
          <p className="text-gray-600 text-lg">Reduce food wastage during festivals and holidays</p>
        </header>

        {/* FORM SECTION - Input Collection */}
        <div className="bg-white rounded-xl shadow-lg p-8 mb-6">
          <form onSubmit={calculatePrediction} className="space-y-6">

            {/* Grid layout for form fields - 2 columns on medium+ screens */}
            <div className="grid md:grid-cols-2 gap-6">

              {/* Festival/Holiday Name Input */}
              <div>
                <label className="block text-sm font-semibold text-gray-700 mb-2">
                  <Calendar className="inline w-4 h-4 mr-1" />
                  Festival / Holiday Name
                </label>
                <input
                  type="text"
                  name="festivalName"
                  value={formData.festivalName}
                  onChange={handleInputChange}
                  required
                  placeholder="e.g., Diwali, Christmas"
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition"
                />
              </div>

              {/* Date Input */}
              <div>
                <label className="block text-sm font-semibold text-gray-700 mb-2">
                  <Calendar className="inline w-4 h-4 mr-1" />
                  Date
                </label>
                <input
                  type="date"
                  name="date"
                  value={formData.date}
                  onChange={handleInputChange}
                  required
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition"
                />
              </div>

              {/* Total Students Input */}
              <div>
                <label className="block text-sm font-semibold text-gray-700 mb-2">
                  <Users className="inline w-4 h-4 mr-1" />
                  Total Students in Hostel
                </label>
                <input
                  type="number"
                  name="totalStudents"
                  value={formData.totalStudents || ''}
                  onChange={handleInputChange}
                  required
                  min="0"
                  placeholder="e.g., 500"
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition"
                />
              </div>

              {/* Veg Students Input */}
              <div>
                <label className="block text-sm font-semibold text-gray-700 mb-2">
                  <Users className="inline w-4 h-4 mr-1" />
                  Number of Veg Students
                </label>
                <input
                  type="number"
                  name="vegStudents"
                  value={formData.vegStudents || ''}
                  onChange={handleInputChange}
                  required
                  min="0"
                  placeholder="e.g., 300"
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition"
                />
              </div>

              {/* Non-Veg Students Input */}
              <div>
                <label className="block text-sm font-semibold text-gray-700 mb-2">
                  <Users className="inline w-4 h-4 mr-1" />
                  Number of Non-Veg Students
                </label>
                <input
                  type="number"
                  name="nonVegStudents"
                  value={formData.nonVegStudents || ''}
                  onChange={handleInputChange}
                  required
                  min="0"
                  placeholder="e.g., 200"
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition"
                />
              </div>

              {/* Meal Type Dropdown */}
              <div>
                <label className="block text-sm font-semibold text-gray-700 mb-2">
                  <Utensils className="inline w-4 h-4 mr-1" />
                  Meal Type
                </label>
                <select
                  name="mealType"
                  value={formData.mealType}
                  onChange={handleInputChange}
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition"
                >
                  <option value="Breakfast">Breakfast</option>
                  <option value="Lunch">Lunch</option>
                  <option value="Dinner">Dinner</option>
                </select>
              </div>
            </div>

            {/* Attendance Percentage Slider */}
            <div>
              <label className="block text-sm font-semibold text-gray-700 mb-2">
                Expected Attendance Percentage: <span className="text-blue-600">{formData.attendancePercentage}%</span>
              </label>
              <input
                type="range"
                name="attendancePercentage"
                value={formData.attendancePercentage}
                onChange={handleInputChange}
                min="0"
                max="100"
                className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-blue-600"
              />
              <div className="flex justify-between text-xs text-gray-500 mt-1">
                <span>0%</span>
                <span>50%</span>
                <span>100%</span>
              </div>
            </div>

            {/* Action Buttons */}
            <div className="flex gap-4 pt-4">
              {/* Submit Button - Triggers calculation */}
              <button
                type="submit"
                className="flex-1 bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-6 rounded-lg transition duration-200 flex items-center justify-center gap-2 shadow-md"
              >
                <Calculator className="w-5 h-5" />
                Calculate Prediction
              </button>

              {/* Reset Button - Clears form */}
              <button
                type="button"
                onClick={handleReset}
                className="px-6 py-3 border-2 border-gray-300 text-gray-700 font-semibold rounded-lg hover:bg-gray-50 transition duration-200"
              >
                Reset
              </button>
            </div>
          </form>
        </div>

        {/* RESULTS SECTION - Only shown after calculation */}
        {showResults && prediction && (
          <div className="bg-white rounded-xl shadow-lg p-8 animate-fadeIn">
            <h2 className="text-2xl font-bold text-gray-800 mb-4 flex items-center gap-2">
              <Calculator className="w-6 h-6 text-green-600" />
              Predicted Food Quantities
            </h2>

            {/* Summary Box - Shows input details and expected attendees */}
            <div className="bg-blue-50 border-l-4 border-blue-600 p-4 mb-6 rounded">
              <p className="text-sm font-semibold text-blue-900">
                Festival: <span className="font-normal">{formData.festivalName}</span>
              </p>
              <p className="text-sm font-semibold text-blue-900">
                Date: <span className="font-normal">{new Date(formData.date).toLocaleDateString('en-IN', { year: 'numeric', month: 'long', day: 'numeric' })}</span>
              </p>
              <p className="text-sm font-semibold text-blue-900">
                Meal Type: <span className="font-normal">{formData.mealType}</span>
              </p>
              <p className="text-sm font-semibold text-blue-900">
                Expected Attendees: <span className="font-normal">{prediction.expectedAttendees} out of {formData.totalStudents} students</span>
              </p>
            </div>

            {/* Grid of Quantity Cards */}
            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">

              {/* Rice Card - Only shown for Lunch/Dinner */}
              {formData.mealType !== 'Breakfast' && (
                <div className="bg-gradient-to-br from-yellow-50 to-yellow-100 p-5 rounded-lg border border-yellow-200">
                  <h3 className="text-lg font-semibold text-gray-700 mb-2">Rice</h3>
                  <p className="text-3xl font-bold text-yellow-700">{prediction.rice} kg</p>
                  <p className="text-xs text-gray-600 mt-1">150g per person</p>
                </div>
              )}

              {/* Vegetables Card */}
              <div className="bg-gradient-to-br from-green-50 to-green-100 p-5 rounded-lg border border-green-200">
                <h3 className="text-lg font-semibold text-gray-700 mb-2">Vegetables</h3>
                <p className="text-3xl font-bold text-green-700">{prediction.vegetables} kg</p>
                <p className="text-xs text-gray-600 mt-1">200g per person</p>
              </div>

              {/* Oil Card */}
              <div className="bg-gradient-to-br from-orange-50 to-orange-100 p-5 rounded-lg border border-orange-200">
                <h3 className="text-lg font-semibold text-gray-700 mb-2">Cooking Oil</h3>
                <p className="text-3xl font-bold text-orange-700">{prediction.oil} L</p>
                <p className="text-xs text-gray-600 mt-1">15ml per person</p>
              </div>

              {/* Dal Card - Only shown for Lunch/Dinner */}
              {formData.mealType !== 'Breakfast' && (
                <div className="bg-gradient-to-br from-amber-50 to-amber-100 p-5 rounded-lg border border-amber-200">
                  <h3 className="text-lg font-semibold text-gray-700 mb-2">Dal / Lentils</h3>
                  <p className="text-3xl font-bold text-amber-700">{prediction.dal} kg</p>
                  <p className="text-xs text-gray-600 mt-1">100g per person</p>
                </div>
              )}

              {/* Chapati Card */}
              <div className="bg-gradient-to-br from-red-50 to-red-100 p-5 rounded-lg border border-red-200">
                <h3 className="text-lg font-semibold text-gray-700 mb-2">Chapati / Roti</h3>
                <p className="text-3xl font-bold text-red-700">{prediction.chapati} pieces</p>
                <p className="text-xs text-gray-600 mt-1">
                  {formData.mealType === 'Breakfast' ? '2' : '3'} per person
                </p>
              </div>
            </div>

            {/* Disclaimer Note */}
            <div className="mt-6 p-4 bg-green-50 border border-green-200 rounded-lg">
              <p className="text-sm text-green-800">
                <strong>Note:</strong> These are estimated quantities based on standard per-person consumption.
                Actual requirements may vary based on cooking method, waste factors, and individual preferences.
              </p>
            </div>
          </div>
        )}

        {/* FOOTER */}
        <footer className="text-center mt-8 text-gray-600 text-sm">
          <p>Hostel Food Quantity Prediction System - Reducing Food Wastage</p>
        </footer>
      </div>
    </div>
  );
}

export default App;
