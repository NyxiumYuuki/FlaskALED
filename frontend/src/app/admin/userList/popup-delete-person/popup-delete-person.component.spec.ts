import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PopupDeletePersonComponent } from './popup-delete-person.component';

describe('PopupDeletePersonComponent', () => {
  let component: PopupDeletePersonComponent;
  let fixture: ComponentFixture<PopupDeletePersonComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PopupDeletePersonComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PopupDeletePersonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
