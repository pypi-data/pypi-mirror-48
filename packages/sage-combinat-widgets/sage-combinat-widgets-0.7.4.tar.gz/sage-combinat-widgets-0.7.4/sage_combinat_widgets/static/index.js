define(["@jupyter-widgets/base","@jupyter-widgets/controls"], function(__WEBPACK_EXTERNAL_MODULE_2__, __WEBPACK_EXTERNAL_MODULE_3__) { return /******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, {
/******/ 				configurable: false,
/******/ 				enumerable: true,
/******/ 				get: getter
/******/ 			});
/******/ 		}
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ (function(module, exports, __webpack_require__) {

// Export widget models and views, and the npm package version number.
module.exports = __webpack_require__(1);
module.exports['version'] = __webpack_require__(4).version;


/***/ }),
/* 1 */
/***/ (function(module, exports, __webpack_require__) {

var widgets = __webpack_require__(2);
var widgets = __webpack_require__(3);

var TextWithTooltipView = widgets.TextView.extend({
    render: function() {
        widgets.TextView.prototype.render.call(this);
        this.update_title();
        this.model.on('change:description_tooltip', this.update_title, this);
    },
    update_title: function() {
        this.textbox.title = this.model.get('description_tooltip');
    }
});

module.exports = {
    TextWithTooltipView : TextWithTooltipView
};


/***/ }),
/* 2 */
/***/ (function(module, exports) {

module.exports = __WEBPACK_EXTERNAL_MODULE_2__;

/***/ }),
/* 3 */
/***/ (function(module, exports) {

module.exports = __WEBPACK_EXTERNAL_MODULE_3__;

/***/ }),
/* 4 */
/***/ (function(module, exports) {

module.exports = {"name":"sage-combinat-widgets","version":"0.1.0","license":"GPL-2.0+","description":"Jupyter widgets for SAGE Combinat","author":"Odile Bénassy, Nicolas Thiéry","main":"lib/index.js","repository":{"type":"git","url":"https://github.com/sagemath/sage-combinat-widgets.git"},"keywords":["jupyter","widgets","ipython","ipywidgets","jupyterlab-extension"],"files":["lib/**/*.js","lib/**/*.css","dist/*.js"],"scripts":{"clean":"rimraf dist/","prepare":"webpack","test":"echo \"Error: no test specified\" && exit 1"},"devDependencies":{"webpack":"^3.5.5","rimraf":"^2.6.1"},"dependencies":{"@jupyter-widgets/base":"^1.0.0","@jupyter-widgets/controls":"^1.0.0","lodash":"^4.17.4","npm":"^6.6.0"},"jupyterlab":{"extension":"lib/labplugin"}}

/***/ })
/******/ ])});;
//# sourceMappingURL=index.js.map