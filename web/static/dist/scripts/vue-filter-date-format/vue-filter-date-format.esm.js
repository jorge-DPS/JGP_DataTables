/*! *****************************************************************************
Copyright (c) Microsoft Corporation.

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
***************************************************************************** */

var __assign = function() {
    __assign = Object.assign || function __assign(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p)) t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};

var version = "1.6.3";

var DateFormats;
(function (DateFormats) {
    DateFormats["DD"] = "DD";
    DateFormats["D"] = "D";
})(DateFormats || (DateFormats = {}));

var HoursFormats;
(function (HoursFormats) {
    HoursFormats["HH"] = "HH";
    HoursFormats["H"] = "H";
    HoursFormats["hh"] = "hh";
    HoursFormats["h"] = "h";
})(HoursFormats || (HoursFormats = {}));

var MillisecondsFormats;
(function (MillisecondsFormats) {
    MillisecondsFormats["SSS"] = "SSS";
    MillisecondsFormats["S"] = "S";
})(MillisecondsFormats || (MillisecondsFormats = {}));

var MinutesFormats;
(function (MinutesFormats) {
    MinutesFormats["mm"] = "mm";
    MinutesFormats["m"] = "m";
})(MinutesFormats || (MinutesFormats = {}));

var MonthFormats;
(function (MonthFormats) {
    MonthFormats["MMMM"] = "MMMM";
    MonthFormats["MMM"] = "MMM";
    MonthFormats["MM"] = "MM";
    MonthFormats["M"] = "M";
})(MonthFormats || (MonthFormats = {}));

var PeriodFormats;
(function (PeriodFormats) {
    PeriodFormats["A"] = "A";
    PeriodFormats["a"] = "a";
})(PeriodFormats || (PeriodFormats = {}));

var SecondsFormats;
(function (SecondsFormats) {
    SecondsFormats["ss"] = "ss";
    SecondsFormats["s"] = "s";
})(SecondsFormats || (SecondsFormats = {}));

var WeekdayFormats;
(function (WeekdayFormats) {
    WeekdayFormats["dddd"] = "dddd";
    WeekdayFormats["dd"] = "dd";
    WeekdayFormats["d"] = "d";
})(WeekdayFormats || (WeekdayFormats = {}));

var YearFormats;
(function (YearFormats) {
    YearFormats["YYYY"] = "YYYY";
    YearFormats["YY"] = "YY";
})(YearFormats || (YearFormats = {}));

function padStart(input, targetLength, padString) {
    if (targetLength === void 0) { targetLength = 0; }
    if (padString === void 0) { padString = ' '; }
    var padSubstring = new Array(targetLength).fill(padString).join('');
    return ("" + padSubstring + input).slice(-targetLength);
}
function padEnd(input, targetLength, padString) {
    if (targetLength === void 0) { targetLength = 0; }
    if (padString === void 0) { padString = ' '; }
    var padSubstring = new Array(targetLength).fill(padString).join('');
    return ("" + input + padSubstring).slice(0, targetLength);
}

function dateTransformer(input, format, config) {
    var date = 'timezone' in config ? input.getUTCDate() : input.getDate();
    if (format === DateFormats.DD) {
        return padStart(date, 2, '0');
    }
    if (format === DateFormats.D) {
        return date.toString();
    }
    throw new Error("[vue-filter-date-format]: Invalid date format '" + format + "'");
}

function hoursTransformer(input, format, config) {
    var hours24 = 'timezone' in config ? input.getUTCHours() : input.getHours();
    var hours12 = hours24 % 12 === 0 ? 12 : hours24 % 12;
    if (format === HoursFormats.HH) {
        return padStart(hours24, 2, '0');
    }
    if (format === HoursFormats.H) {
        return hours24.toString();
    }
    if (format === HoursFormats.hh) {
        return padStart(hours12, 2, '0');
    }
    if (format === HoursFormats.h) {
        return hours12.toString();
    }
    throw new Error("[vue-filter-date-format]: Invalid hours format '" + format + "'");
}

function millisecondsTransformer(input, format, config) {
    var milliseconds = 'timezone' in config ? input.getUTCMilliseconds() : input.getMilliseconds();
    if (format === MillisecondsFormats.SSS) {
        return padEnd(milliseconds, 3, '0');
    }
    if (format === MillisecondsFormats.S) {
        return milliseconds.toString();
    }
    throw new Error("[vue-filter-date-format]: Invalid milliseconds format '" + format + "'");
}

function minutesTransformer(input, format, config) {
    var minutes = 'timezone' in config ? input.getUTCMinutes() : input.getMinutes();
    if (format === MinutesFormats.mm) {
        return padStart(minutes, 2, '0');
    }
    if (format === MinutesFormats.m) {
        return minutes.toString();
    }
    throw new Error("[vue-filter-date-format]: Invalid minutes format '" + format + "'");
}

function monthTransformer(input, format, config) {
    var month = ('timezone' in config ? input.getUTCMonth() : input.getMonth()) + 1;
    if (format === MonthFormats.MMMM) {
        return config.monthNames[month - 1];
    }
    if (format === MonthFormats.MMM) {
        return config.monthNamesShort[month - 1];
    }
    if (format === MonthFormats.MM) {
        return padStart(month, 2, '0');
    }
    if (format === MonthFormats.M) {
        return month.toString();
    }
    throw new Error("[vue-filter-date-format]: Invalid month format '" + format + "'");
}

function periodTransformer(input, format, config) {
    var hours24 = 'timezone' in config ? input.getUTCHours() : input.getHours();
    if (format === PeriodFormats.A) {
        return hours24 < 12 ? 'AM' : 'PM';
    }
    if (format === PeriodFormats.a) {
        return hours24 < 12 ? 'am' : 'pm';
    }
    throw new Error("[vue-filter-date-format]: Invalid period format '" + format + "'");
}

function secondsTransformer(input, format, config) {
    var seconds = 'timezone' in config ? input.getUTCSeconds() : input.getSeconds();
    if (format === SecondsFormats.ss) {
        return padStart(seconds, 2, '0');
    }
    if (format === SecondsFormats.s) {
        return seconds.toString();
    }
    throw new Error("[vue-filter-date-format]: Invalid seconds format '" + format + "'");
}

function weekdayTransformer(input, format, config) {
    var weekday = 'timezone' in config ? input.getUTCDay() : input.getDay();
    if (format === WeekdayFormats.dddd) {
        return config.dayOfWeekNames[weekday];
    }
    if (format === WeekdayFormats.dd) {
        return config.dayOfWeekNamesShort[weekday];
    }
    if (format === WeekdayFormats.d) {
        return weekday.toString();
    }
    throw new Error("[vue-filter-date-format]: Invalid weekday format '" + format + "'");
}

function yearTransformer(input, format, config) {
    var year = 'timezone' in config ? input.getUTCFullYear() : input.getFullYear();
    if (format === YearFormats.YYYY) {
        return padStart(year, 4, '0');
    }
    if (format === YearFormats.YY) {
        return padStart(year % 100, 2, '0');
    }
    throw new Error("[vue-filter-date-format]: Invalid year format '" + format + "'");
}

var defaultConfig = {
    dayOfWeekNames: [
        'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday'
    ],
    dayOfWeekNamesShort: [
        'Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa'
    ],
    monthNames: [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ],
    monthNamesShort: [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ],
    dateTransformer: dateTransformer,
    hoursTransformer: hoursTransformer,
    millisecondsTransformer: millisecondsTransformer,
    minutesTransformer: minutesTransformer,
    monthTransformer: monthTransformer,
    periodTransformer: periodTransformer,
    secondsTransformer: secondsTransformer,
    weekdayTransformer: weekdayTransformer,
    yearTransformer: yearTransformer
};
function dateFormat(input, format, customConfig) {
    if (format === void 0) { format = 'YYYY-MM-DD HH:mm:ss'; }
    if (customConfig === void 0) { customConfig = {}; }
    var config = __assign(__assign({}, defaultConfig), customConfig);
    if ('timezone' in config) {
        input = new Date(input.getTime());
        input.setMinutes(input.getMinutes() + config.timezone);
    }
    return format
        // Normalize tokens
        .replace(YearFormats.YYYY, '%01%')
        .replace(YearFormats.YY, '%02%')
        .replace(MonthFormats.MMMM, '%03%')
        .replace(MonthFormats.MMM, '%04%')
        .replace(MonthFormats.MM, '%05%')
        .replace(MonthFormats.M, '%06%')
        .replace(DateFormats.DD, '%07%')
        .replace(DateFormats.D, '%08%')
        .replace(HoursFormats.HH, '%09%')
        .replace(HoursFormats.H, '%10%')
        .replace(HoursFormats.hh, '%11%')
        .replace(HoursFormats.h, '%12%')
        .replace(MinutesFormats.mm, '%13%')
        .replace(MinutesFormats.m, '%14%')
        .replace(SecondsFormats.ss, '%15%')
        .replace(SecondsFormats.s, '%16%')
        .replace(PeriodFormats.A, '%17%')
        .replace(PeriodFormats.a, '%18%')
        .replace(WeekdayFormats.dddd, '%19%')
        .replace(WeekdayFormats.dd, '%20%')
        .replace(WeekdayFormats.d, '%21%')
        .replace(MillisecondsFormats.SSS, '%22%')
        .replace(MillisecondsFormats.S, '%23%')
        // Insert values
        .replace('%01%', yearTransformer(input, YearFormats.YYYY, config))
        .replace('%02%', yearTransformer(input, YearFormats.YY, config))
        .replace('%03%', monthTransformer(input, MonthFormats.MMMM, config))
        .replace('%04%', monthTransformer(input, MonthFormats.MMM, config))
        .replace('%05%', monthTransformer(input, MonthFormats.MM, config))
        .replace('%06%', monthTransformer(input, MonthFormats.M, config))
        .replace('%07%', dateTransformer(input, DateFormats.DD, config))
        .replace('%08%', dateTransformer(input, DateFormats.D, config))
        .replace('%09%', hoursTransformer(input, HoursFormats.HH, config))
        .replace('%10%', hoursTransformer(input, HoursFormats.H, config))
        .replace('%11%', hoursTransformer(input, HoursFormats.hh, config))
        .replace('%12%', hoursTransformer(input, HoursFormats.h, config))
        .replace('%13%', minutesTransformer(input, MinutesFormats.mm, config))
        .replace('%14%', minutesTransformer(input, MinutesFormats.m, config))
        .replace('%15%', secondsTransformer(input, SecondsFormats.ss, config))
        .replace('%16%', secondsTransformer(input, SecondsFormats.s, config))
        .replace('%17%', periodTransformer(input, PeriodFormats.A, config))
        .replace('%18%', periodTransformer(input, PeriodFormats.a, config))
        .replace('%19%', weekdayTransformer(input, WeekdayFormats.dddd, config))
        .replace('%20%', weekdayTransformer(input, WeekdayFormats.dd, config))
        .replace('%21%', weekdayTransformer(input, WeekdayFormats.d, config))
        .replace('%22%', millisecondsTransformer(input, MillisecondsFormats.SSS, config))
        .replace('%23%', millisecondsTransformer(input, MillisecondsFormats.S, config));
}
var vueFilterDateFormat = {
    install: function (Vue, baseConfig) {
        Vue.filter('dateFormat', function (date, format, config) {
            if (config === void 0) { config = {}; }
            return dateFormat(date, format, __assign(__assign({}, baseConfig), config));
        });
    },
    version: version
};

export default vueFilterDateFormat;
export { dateFormat };
//# sourceMappingURL=vue-filter-date-format.esm.js.map
