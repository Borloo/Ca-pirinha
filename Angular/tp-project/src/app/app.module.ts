import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeroListComponent } from './heroes/hero-list/hero-list.component';
import { ReactiveFormsModule } from '@angular/forms';
import { DatePipePipe } from './heroes/date-pipe.pipe';
import { TestComponent } from './heroes/test/test.component';
import {HeroListService} from "./heroes/hero-list/hero-list.service";
import {HeroListDirective} from "./heroes/hero-list/hero-list.directive";

@NgModule({
  declarations: [
    AppComponent,
    HeroListComponent,
    DatePipePipe,
    TestComponent,
    HeroListDirective,
    HeroListDirective
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule
  ],
  providers: [
    HeroListService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
