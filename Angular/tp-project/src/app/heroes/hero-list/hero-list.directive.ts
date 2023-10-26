import {Directive, ElementRef} from '@angular/core';

@Directive({
  selector: '[appHighLight]'
})
export class HeroListDirective {

  constructor(private el: ElementRef) {
    this.el.nativeElement.style.backgroundColor = 'yellow';
  }

}
