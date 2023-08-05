/* global angular */
'use strict';

/**
 * Main App Module
 */

let app = angular.module('app', ['utils', 'search', 'ngAnimate', 'ui.bootstrap', 'ng.jsoneditor'])
    .controller('ALController', function ($scope, $http, $timeout) {
        //Parameters lets
        $scope.user = null;
        $scope.options = null;
        $scope.loading = false;
        $scope.loading_extra = false;
        $scope.sha256 = null;
        $scope.tag_map = null;
        $scope.current_file = null;
        $scope.selected_highlight = [];
        $scope.splitter = "__";
        $scope.switch_service = null;

        //DEBUG MODE
        $scope.debug = false;
        $scope.showParams = function () {
            console.log("Scope", $scope)
        };

        $scope.select_alternate = function (service, created) {
            $scope.loading_extra = true;
            $timeout(function () {
                for (let key in $scope.current_file.alternates[service]) {
                    let item = $scope.current_file.alternates[service][key];
                    if (item.created === created) {
                        for (let i in $scope.current_file.results) {
                            if ($scope.current_file.results[i].response.service_name === service) {
                                if (item.id !== undefined) {
                                    $http({
                                        method: 'GET',
                                        url: "/api/v4/result/" + item.id + "/"
                                    })
                                        .success(function (data) {
                                            $scope.current_file.results[i] = data.api_response;
                                            $scope.current_file.alternates[service][key] = data.api_response;
                                            $scope.switch_service = service;
                                            $scope.loading_extra = false;
                                        })
                                        .error(function (data, status, headers, config) {
                                            if (data === "" || data === null) {
                                                return;
                                            }

                                            $scope.loading_extra = false;
                                            if (data.api_error_message) {
                                                $scope.error = data.api_error_message;
                                            }
                                            else {
                                                $scope.error = config.url + " (" + status + ")";
                                            }

                                        });
                                }
                                else {
                                    $scope.current_file.results[i] = item;
                                    $scope.switch_service = service;
                                    $scope.loading_extra = false;
                                }
                                break;
                            }
                        }
                        break;
                    }
                }
            }, 0);

        };

        //Filters
        let tagTypes = [];
        $scope.tagTypeList = function (myTagList) {
            tagTypes = [];
            if (myTagList === undefined || myTagList == null) return [];
            return myTagList;
        };

        $scope.filterTagType = function (tag) {
            let isNewType = tagTypes.indexOf(tag.type) === -1;
            if (isNewType) {
                tagTypes.push(tag.type);
            }
            return isNewType;
        };

        $scope.useless_results = function () {
            return function (item) {
                return !(item.result.score === 0 && item.result.sections.length === 0 && item.result.tags.length === 0 && item.response.extracted.length === 0);

            }
        };

        $scope.good_results = function () {
            return function (item) {
                return item.result.score === 0 && item.result.sections.length === 0 && item.result.tags.length === 0 && item.response.extracted.length === 0;

            }
        };

        $scope.sort_by_name = function (item) {
            return item.response.service_name;
        };

        $scope.obj_len = function (o) {
            if (o === undefined || o == null) return 0;
            return Object.keys(o).length;
        };

        //Action
        $scope.uri_encode = function (val) {
            return encodeURIComponent(val)
        };

        $scope.search_tag = function (tag, value) {
            window.location = "/search.html?query=result.tags.type:" + encodeURIComponent(tag) + " AND result.tags.value:" + encodeURIComponent(value)
        };

        $scope.dump = function (obj) {
            return angular.toJson(obj, true);
        };

        $scope.resubmit_dynamic_async = function (sha256) {
            $scope.error = '';
            $scope.success = '';
            $scope.loading_extra = true;

            $http({
                method: 'GET',
                url: "/api/v4/submit/dynamic/" + sha256 + "/"
            })
                .success(function (data) {
                    $scope.loading_extra = true;
                    $scope.success = 'File successfully resubmitted for dynamic analysis. You will be redirected...';
                    $timeout(function () {
                        $scope.success = "";
                        window.location = "/submission_detail.html?sid=" + data.api_response.sid;
                    }, 2000);
                })
                .error(function (data, status, headers, config) {
                    if (data === "" || data === null) {
                        return;
                    }

                    $scope.loading_extra = false;
                    if (data.api_error_message) {
                        $scope.error = data.api_error_message;
                    }
                    else {
                        $scope.error = config.url + " (" + status + ")";
                    }

                });
        };

        //Highlighter
        $scope.trigger_highlight = function (tag, value) {
            let key = tag + $scope.splitter + value;
            let idx = $scope.selected_highlight.indexOf(key);
            if (idx === -1) {
                $scope.selected_highlight.push(key);
            }
            else {
                $scope.selected_highlight.splice(idx, 1);
            }
        };

        $scope.remove_highlight = function (key) {
            let values = key.split($scope.splitter, 2);
            $scope.trigger_highlight(values[0], values[1])
        };

        $scope.isHighlighted = function (tag, value) {
            return $scope.selected_highlight.indexOf(tag + $scope.splitter + value) !== -1
        };

        $scope.hasContext = function (tag) {
            return tag.context != null;
        };

        $scope.hasHighlightedTags = function (tags) {
            for (let i in tags) {
                let tag = tags[i];
                if ($scope.isHighlighted(tag.type, tag.value)) {
                    return true;
                }
            }
            return false;
        };

        $scope.clear_selection = function () {
            $scope.selected_highlight = [];
        };

        //Error handling
        $scope.error = '';

        //Load params from datastore
        $scope.start = function () {
            $scope.loading_extra = true;
            $http({
                method: 'GET',
                url: "/api/v4/file/result/" + $scope.sha256 + "/"
            })
                .success(function (data) {
                    $scope.current_file = data.api_response;
                    for (let key in $scope.current_file.results) {
                        let item = $scope.current_file.results[key];
                        if (item.response.service_name in $scope.current_file.alternates) {
                            $scope.current_file.alternates[item.response.service_name].unshift(item);
                        }
                        else {
                            $scope.current_file.alternates[item.response.service_name] = [item];
                        }
                    }
                    $scope.loading_extra = false;
                })
                .error(function (data, status, headers, config) {
                    if (data === "" || data === null) {
                        return;
                    }

                    $scope.loading_extra = false;
                    if (data.api_error_message) {
                        $scope.error = data.api_error_message;
                    }
                    else {
                        $scope.error = config.url + " (" + status + ")";
                    }

                });
        };

    });

