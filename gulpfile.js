/* global require */

var gulp = require('gulp');
var usemin = require('gulp-usemin');
var uglify = require('gulp-uglify');
var minifyHtml = require('gulp-minify-html');
var minifyCss = require('gulp-minify-css');
var rev = require('gulp-rev');

gulp.task('usemin', function() {
    'use strict';

    gulp.src('app/templates/*.html')
        .pipe(usemin({
            css: [minifyCss(), 'concat'],
            html: [minifyHtml({empty: true, loose:true})],
            js: [uglify(), rev()]
        }))
        .pipe(gulp.dest('app/templates/dist/'));
});
