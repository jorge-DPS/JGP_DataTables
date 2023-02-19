"use strict";var KTDatatablesExtensionsFixedheader={init:function(){$("#kt_table_1").DataTable({responsive:!0,fixedHeader:{header:!0,headerOffset:$("#kt_header").height()},paging:!1,columnDefs:[{targets:-1,title:"Actions",orderable:!1,render:function(e,a,t,l){return`
                        <span class="dropdown">
                            <a href="#" class="btn btn-sm btn-clean btn-icon btn-icon-md" data-toggle="dropdown" aria-expanded="true">
                              <i class="la la-ellipsis-h"></i>
                            </a>
                            <div class="dropdown-menu dropdown-menu-right">
                                <a class="dropdown-item" href="#"><i class="la la-edit"></i> Edit Details</a>
                                <a class="dropdown-item" href="#"><i class="la la-leaf"></i> Update Status</a>
                                <a class="dropdown-item" href="#"><i class="la la-print"></i> Generate Report</a>
                            </div>
                        </span>
                        <a href="#" class="btn btn-sm btn-clean btn-icon btn-icon-md" title="View">
                          <i class="la la-edit"></i>
                        </a>`}},{width:"75px",targets:8,render:function(e,a,t,l){var s={1:{title:"Pending",class:"label-primary"},2:{title:"Delivered",class:" label-danger"},3:{title:"Canceled",class:" label-primary"},4:{title:"Success",class:" label-success"},5:{title:"Info",class:" label-info"},6:{title:"Danger",class:" label-danger"},7:{title:"Warning",class:" label-warning"}};return void 0===s[e]?e:'<span class="label '+s[e].class+' label-inline label-pill">'+s[e].title+"</span>"}},{width:"75px",targets:9,render:function(e,a,t,l){var s={1:{title:"Online",state:"danger"},2:{title:"Retail",state:"primary"},3:{title:"Direct",state:"success"}};return void 0===s[e]?e:'<span class="label label-'+s[e].state+' label-dot"></span>&nbsp;<span class="font-weight-bold text-'+s[e].state+'">'+s[e].title+"</span>"}}]})}};jQuery(document).ready(function(){KTDatatablesExtensionsFixedheader.init()});