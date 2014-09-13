/* global require */

var gulp = require('gulp');
var usemin = require('gulp-usemin');
var uglify = require('gulp-uglify');
var minifyHtml = require('gulp-minify-html');
var minifyCss = require('gulp-minify-css');
var rev = require('gulp-rev');
var clean = require('gulp-clean');

gulp.task('dist', ['usemin'], function() {
    'use strict';

    // move css files
    var files = [
        'app/templates/dist/static/dist/*.css',
        'app/templates/dist/static/dist/*.js'
    ];

    gulp.src(files, {base: 'app/templates/dist/static/'})
        .pipe(gulp.dest('app/static/'));
});

gulp.task('usemin', function() {
    'use strict';

    gulp.src('app/templates/*.html')
        .pipe(usemin({
            css: [minifyCss(), 'concat'],
            js: [uglify(), 'concat']
        }))
        .pipe(gulp.dest('app/templates/dist'));
});

gulp.task('clean', function() {
    'use strict';

    var dirs = [
        'app/templates/dist',
        'app/static/dist'
    ];

    gulp.src(dirs, {read: false})
        .pipe(clean());
});
