import { VueConstructor } from 'vue';
interface IDateFormatConfig {
    dayOfWeekNames: string[];
    dayOfWeekNamesShort: string[];
    monthNames: string[];
    monthNamesShort: string[];
    timezone?: number;
    dateTransformer: Function;
    hoursTransformer: Function;
    millisecondsTransformer: Function;
    minutesTransformer: Function;
    monthTransformer: Function;
    periodTransformer: Function;
    secondsTransformer: Function;
    weekdayTransformer: Function;
    yearTransformer: Function;
}
declare function dateFormat(input: Date, format?: string, customConfig?: Partial<IDateFormatConfig>): string;
declare const _default: {
    install(Vue: VueConstructor, baseConfig: Partial<IDateFormatConfig>): void;
    version: string;
};
export { _default as default, IDateFormatConfig, dateFormat };
