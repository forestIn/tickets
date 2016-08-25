gulp = require 'gulp'
stylus = require 'gulp-stylus'
coffee = require 'gulp-coffee'
# uglify = require 'gulp-uglify'
clean = require 'gulp-clean'
concat = require 'gulp-concat'
# ngAnnotate = require 'gulp-ng-annotate' #Add angularjs dependency injection annotations with ng-annotate


gulp.task 'stylus', ->
    gulp.src 'front/stylus/*.styl'
        .pipe stylus set: ['compress']
        .pipe gulp.dest 'static/css'
        # .pipe do connect.reload



gulp.task 'coffee', ->
    gulp.src 'front/coffee/dispatcher/*.coffee'
        .pipe do coffee
        # .pipe ngAnnotate()
        # .pipe concat 'all.js'
        # .pipe uglify()
        .pipe gulp.dest 'static/js/dispatcher'
        # .pipe do connect.reload

gulp.task 'watch', ->
    # gulp.watch 'dist/*.html', ['html']
    gulp.watch 'front/stylus/*.styl', ['stylus']
    gulp.watch 'front/coffee/dispatcher/*.coffee', ['coffee']

gulp.task 'default', ['coffee', 'stylus','watch']