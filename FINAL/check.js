const babel = require('@babel/core');
const fs = require('fs');
const file = fs.readFileSync('admin_attendance.html', 'utf8');
const scriptMatch = file.match(/<script type="text\/babel" data-type="module">([\s\S]*?)<\/script>/);
if (!scriptMatch) {
  console.log('No Babel script found.');
  process.exit(1);
}
const code = scriptMatch[1];
try {
  babel.transformSync(code, { presets: ['@babel/preset-react'] });
  console.log('JSX parsed successfully! NO ERRORS');
} catch (e) {
  console.error(e.message);
}
