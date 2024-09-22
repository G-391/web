/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
     './templates/**/*.html'
  ],
  theme: {
    extend: {
      fontFamily :{
        angsana : ["Angsana New"],
        sarabun : ["Sarabun"],
        mitr : ["Mitr"],
        prompt : ["Prompt"],


      }
    },
  },
  plugins: [],
}

