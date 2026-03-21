/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html", "./src/**/*.{js,ts,jsx,tsx,css,scss}"],
  theme: {
    extend: {
      colors: {
        ink: "#1f1d24",
        paper: "#f9f5ef",
        ember: "#cf4b2e",
      },
    },
  },
  plugins: [],
}

