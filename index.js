const { grab } = require('browser-screen-grab');

const interval = 5 * 1000;
const url = 'https://www.google.de/maps/@48.7933017,9.1715786,12z/data=!5m1!1e1';

grab(interval, url, `${__dirname}/stuttgart`, 'stuttgart');
