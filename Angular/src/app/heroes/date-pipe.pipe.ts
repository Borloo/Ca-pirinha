import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'datePipe'
})
export class DatePipePipe implements PipeTransform {

  transform(value: any) {
    let lastChar = value[value.length - 1];

    if (lastChar === "0") {
      return value + ' !';
    } else {
      return value;
    }
  }

}
