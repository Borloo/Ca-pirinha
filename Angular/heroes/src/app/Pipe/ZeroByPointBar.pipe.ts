import { Pipe, PipeTransform } from "@angular/core";

@Pipe({name: 'zeroByPointBar'})
export class ZeroByPointBar implements PipeTransform {
    transform(value: any) {
        let lastChar = value[value.length - 1];
        if(lastChar === '0'){
            return value + "!";
        }
        return value;
    }
}