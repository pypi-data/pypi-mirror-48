define(["@jupyter-widgets/base"], function(__WEBPACK_EXTERNAL_MODULE_2__) { return /******/ (function(modules) { // webpackBootstrap
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
module.exports['version'] = __webpack_require__(3).version;


/***/ }),
/* 1 */
/***/ (function(module, exports, __webpack_require__) {

var widgets = __webpack_require__(2);
// var _ = require('lodash');


// Custom Model. Custom widgets models must at least provide default values
// for model attributes, including
//
//  - `_view_name`
//  - `_view_module`
//  - `_view_module_version`
//
//  - `_model_name`
//  - `_model_module`
//  - `_model_module_version`
//
//  when different from the base class.

// When serialiazing the entire widget state for embedding, only values that
// differ from the defaults will be specified.
var IntervalModel = widgets.DOMWidgetModel.extend({
    defaults: _.extend(widgets.DOMWidgetModel.prototype.defaults(), {
        _model_name : 'IntervalModel',
        _view_name : 'IntervalView',
        _model_module : 'jupyter-interval-widget',
        _view_module : 'jupyter-interval-widget',
        _model_module_version : '0.1.0',
        _view_module_version : '0.1.0',
        value : 1000
    })
});


// Custom View. Renders the widget model.
var IntervalView = widgets.DOMWidgetView.extend({
    render: function() {
        this.value_changed();
        this.model.on('change:value', this.value_changed, this);

        var model = this.model;
        var that = this;

        that.on("remove", function(e){
            clearInterval(that.interval);
        }, this);
    },

    value_changed: function() {
        var that = this;
        var value = this.model.get('value');

        clearInterval(this.interval);

        if (value){
            this.interval = setInterval(function() {
                that.send({event: 'tick'});
            }, value);
        }
    },

});


module.exports = {
    IntervalModel : IntervalModel,
    IntervalView : IntervalView
};


/***/ }),
/* 2 */
/***/ (function(module, exports) {

module.exports = __WEBPACK_EXTERNAL_MODULE_2__;

/***/ }),
/* 3 */
/***/ (function(module, exports) {

module.exports = {"name":"jupyter-interval-widget","version":"0.1.0","description":"Jupyter Interval Widget","author":"Samuel Rizzo","main":"lib/index.js","repository":{"type":"git","url":"https://github.com/srizzo/jupyter-interval-widget.git"},"keywords":["jupyter","widgets","ipython","ipywidgets","jupyterlab-extension"],"files":["lib/**/*.js","dist/*.js"],"scripts":{"clean":"rimraf dist/","prepublish":"webpack","build":"webpack","watch":"webpack --watch --mode=development","test":"echo \"Error: no test specified\" && exit 1"},"devDependencies":{"webpack":"^3.5.5","rimraf":"^2.6.1"},"dependencies":{"@jupyter-widgets/base":"^1.0.0","lodash":"^4.17.4"},"jupyterlab":{"extension":"lib/labplugin"}}

/***/ })
/******/ ])});;
//# sourceMappingURL=index.js.map