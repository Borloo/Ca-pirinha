import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {HeroListComponent} from './heroes/hero-list/hero-list.component';
import {ReactiveFormsModule} from '@angular/forms';
import {DatePipePipe} from './heroes/date-pipe.pipe';
import {TestComponent} from './heroes/test/test.component';
import {HeroService} from "./hero.service";
import {HighlightDirective} from './highlight.directive';

@NgModule({
  declarations: [
    AppComponent,
    HeroListComponent,
    DatePipePipe,
    TestComponent,
    HighlightDirective
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule
  ],
  providers: [
    HeroService
  ],
  bootstrap: [AppComponent]
})
export class AppModule {
}
