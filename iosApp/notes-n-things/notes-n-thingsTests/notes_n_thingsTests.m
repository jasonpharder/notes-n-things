//
//  notes_n_thingsTests.m
//  notes-n-thingsTests
//
//  Created by Kyle Derrett on 2/26/2014.
//  Copyright (c) 2014 Comp4350. All rights reserved.
//

#import "notes_n_thingsTests.h"

@implementation notes_n_thingsTests

- (void)setUp
{
    [super setUp];
    
    // Set-up code here.
}

- (void)tearDown
{
    // Tear-down code here.
    
    [super tearDown];
}

- (void)testLogin
{
    //login relies on NSUserDefaults test them to make sure it works
    
    //they can be set to empty strings and not remain nil
    [[NSUserDefaults standardUserDefaults] setObject:@"" forKey:@"email"];
    [[NSUserDefaults standardUserDefaults] setObject:@"" forKey:@"password"];
    [[NSUserDefaults standardUserDefaults] setObject:@"" forKey:@"uid"];
    STAssertNotNil([[NSUserDefaults standardUserDefaults] stringForKey:@"email"], @"Can't set user default email with empty string");
    STAssertNotNil([[NSUserDefaults standardUserDefaults] stringForKey:@"password"], @"Can't set user default password with empty string");
    STAssertNotNil([[NSUserDefaults standardUserDefaults] stringForKey:@"uid"], @"Can't set user default uid with empty string");
    
    //they can be set to specific values
    [[NSUserDefaults standardUserDefaults] setObject:@"someEmail" forKey:@"email"];
    [[NSUserDefaults standardUserDefaults] setObject:@"somePass" forKey:@"password"];
    [[NSUserDefaults standardUserDefaults] setObject:@"1" forKey:@"uid"];
    STAssertEquals([[NSUserDefaults standardUserDefaults] stringForKey:@"email"], @"someEmail", @"Can't set user default email with string");
    STAssertEquals([[NSUserDefaults standardUserDefaults] stringForKey:@"password"], @"somePass", @"Can't set user default password with empty string");
    STAssertEquals([[NSUserDefaults standardUserDefaults] stringForKey:@"uid"], @"1", @"Can't set user default uid with empty string");
    
    //can be set to empty strings after being set to a string
    [[NSUserDefaults standardUserDefaults] setObject:@"" forKey:@"email"];
    [[NSUserDefaults standardUserDefaults] setObject:@"" forKey:@"password"];
    [[NSUserDefaults standardUserDefaults] setObject:@"" forKey:@"uid"];
    STAssertEquals([[NSUserDefaults standardUserDefaults] stringForKey:@"email"], @"", @"Can't set user default email with string");
    STAssertEquals([[NSUserDefaults standardUserDefaults] stringForKey:@"password"], @"", @"Can't set user default password with empty string");
    STAssertEquals([[NSUserDefaults standardUserDefaults] stringForKey:@"uid"], @"", @"Can't set user default uid with empty string");
}

@end
